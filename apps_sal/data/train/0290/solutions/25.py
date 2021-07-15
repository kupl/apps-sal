class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        mem = collections.defaultdict()
        
        def dp(i, j):
            if (i, j) in mem:
                return mem[(i,j)]
            ans = float('inf')
            can_cut = False
            for c in cuts:
                if i < c < j:
                    ans = min(ans, dp(i, c) + dp(c, j) + j - i)
                    can_cut = True
            if not can_cut:
                ans = 0
            mem[(i,j)] = ans
            return ans
        
        ans = dp(0, n)
        # print(mem)
        return ans
