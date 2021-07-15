class Solution:
    
    def winnerSquareGame2(self, n):
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = not all(dp[i - k * k] for k in range(1, int(i**0.5) + 1))
        return dp[-1]
    
    def winnerSquareGame(self, n: int) -> bool:
        # 尝试同样的解法？
        # solve(s), s=当前的剩余的数字下，score diff? 需要的最小步数？
        # 如果s=0，则返回False
        # 如果s=任意一个平方数，则return True, 因为alice可以都拿走
        # 否则，alice可以从中切走任意大小的平方数x，然后把剩下的s-x扔给bob
        
        # 只要其中有一个切割，bob无法在s-x下获胜，那就是alice获胜
        # 如果bob在所有切割下都获胜，那alice lose
        
        # 只从alice的角度出发，是否足够？
        cache = dict()
        
        def solve(s):
            if s in cache: return cache[s]
            if s == 0: 
                cache[s] = False
                return False
            
            if pow(int(sqrt(s)), 2) == s: 
                cache[s] = True
                return True # s is a square number and current player can take it directly, so win
            
            iswin = False
            #for x in range(s-1, 0, -1): # from 1 to s-1, since s is not a square number
            #    if pow(int(sqrt(x)), 2) == x:
            #        if not solve(s-x):
            #            iswin = True
            #            break
            for k in range(1, int(sqrt(s))+1):
                if not solve(s - k*k):
                    iswin = True
                    break
                
            cache[s] = iswin
            return iswin
        return solve(n) # 方法是对的，但是超时了，n=31250的时候

