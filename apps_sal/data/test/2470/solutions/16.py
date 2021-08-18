import bisect
import functools


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(set(arr2))

        @functools.lru_cache(None)
        def dfs(prev, i):
            if i == len(arr1):
                return 0
            j = bisect.bisect_right(arr2, prev)
            swap = 1 + dfs(arr2[j], i + 1) if j < len(arr2) else float('inf')
            noswap = dfs(arr1[i], i + 1) if prev < arr1[i] else float('inf')
            return min(swap, noswap)
        changes = dfs(float('-inf'), 0)
        return changes if changes != float('inf') else -1
