class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # take 1, 2, or 3 stones from the first remaining stones of the row
        
        # memorized dp, with mimmax process
        
        # state = dp[s], start from index s
        
        # take one, stoneValue[s] - dp[s+1]
        # take two, stoneValue[s,s+1] - dp[s+2]
        # take three, stoneValue[s, s+1, s+2] - dp[s+3]
        # max value of these three branches
        
        # dp[s] > 0
        
        memo = {}
        n = len(stoneValue)
        
        def dp(s):
            if s>=n: return 0
            if s in memo:
                return memo[s]
            
            ans = -2**31
            for i in range(1, 4):
                if s + i > n: # was bad, s+i>=n was not correct!
                    break
                ans = max(ans, sum(stoneValue[s:s+i]) - dp(s+i))
            memo[s] = ans
            return ans
        
        score = dp(0) - sum(stoneValue)/2
        #print(score, sum(stoneValue)/2)
        return 'Alice' if score > 0 else 'Bob' if score < 0 else 'Tie'
        
    def stoneGameIII(self, stoneValue: List[int]) -> str:       
        # 采用和类似于stoneGameII的方法，可以吗？-> works!! great 太好了，get一个minmax的求解的模板！！！
        # 残局
        # solve(s) score diff
        # M=1,2,3
        # x=[1,2,3]
        # solve(s) = max(sum(sv[s:s+x-1]) - solve(s+x))
        
        n = len(stoneValue)
        
        cache = dict() # s:score
        
        def solve(s):
            if s>=n: return 0
            if s in cache: return cache[s]
            
            best = -2**31
            presum = 0
            
            for x in range(1, 4):
                if s+x-1 >= n:
                    break
                presum += stoneValue[s+x-1]
                best = max(best, presum - solve(s+x))
            cache[s] = best
            return best
        score = solve(0)
        return 'Alice' if score > 0 else 'Bob' if score < 0 else 'Tie'
