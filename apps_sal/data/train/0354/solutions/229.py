class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        
        memo = {}
        def dfs(last, s,  k):
            if k == n:
                return 1
            if (last, s, k)  in memo:
                return memo[last, s, k]
            
            else:
                
                res = 0
                for i in range(6):
                    if i == last:
                        if s + 1 > rollMax[i]:
                            continue
                        else:
                            res += dfs(i, s+1, k+1)
                    else:
                        res += dfs(i, 1, k+1)
                memo[last, s, k] = res
            return res
        
        
        mode = 10**9 + 7
        return dfs(None, 0, 0)%mode

