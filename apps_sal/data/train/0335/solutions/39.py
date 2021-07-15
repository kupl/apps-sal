from functools import lru_cache
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        # rods = sorted(rods)[::-1]
        n = len(rods)
        psum = rods.copy()
        for i in range(n-1)[::-1]:
            psum[i] += psum[i+1]

        @lru_cache(None)
        def dfs(idx, diff):
            if idx == n:
                return 0 if diff == 0 else -float('inf')
            if diff > psum[idx]:
                return -float('inf')
            return max(dfs(idx+1,diff),dfs(idx+1,diff+rods[idx]),dfs(idx+1,abs(diff-rods[idx]))+min(diff,rods[idx]))
        return dfs(0,0)
