from functools import lru_cache


class Solution:

    def maxJumps(self, arr: List[int], d: int) -> int:

        @lru_cache(None)
        def jump(idx):
            (l, r) = (idx - 1, idx + 1)
            (ans, lans, rans) = (1, 0, 0)
            while l >= max(idx - d, 0) and arr[idx] > arr[l]:
                lans = max(lans, jump(l))
                l -= 1
            while r <= min(len(arr) - 1, idx + d) and arr[idx] > arr[r]:
                rans = max(rans, jump(r))
                r += 1
            return ans + max(rans, lans)
        ans = 0
        for i in range(len(arr)):
            ans = max(ans, jump(i))
        return ans
