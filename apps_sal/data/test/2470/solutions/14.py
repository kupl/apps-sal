from bisect import bisect_right as br
import functools


class Solution:

    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(set(arr2))

        @lru_cache(None)
        def dfs(i, prev):
            if i >= len(arr1):
                return 0
            j = br(arr2, prev)
            swap = 1 + dfs(i + 1, arr2[j]) if j < len(arr2) else math.inf
            noswap = dfs(i + 1, arr1[i]) if arr1[i] > prev else math.inf
            return min(swap, noswap)
        ans = dfs(0, -math.inf)
        return ans if ans != math.inf else -1
