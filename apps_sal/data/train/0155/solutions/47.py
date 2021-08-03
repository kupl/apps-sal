import functools


class Solution:
    def maxJumps(self, arr, d: int) -> int:

        @functools.lru_cache(None)
        def helper(i):
            ans = 1
            for index in range(i + 1, min(len(arr), i + d + 1)):
                if arr[i] > arr[index]:
                    ans = max(ans, 1 + helper(index))
                else:
                    break

            for index in range(i - 1, max(-1, i - d - 1), -1):
                if arr[i] > arr[index]:
                    ans = max(ans, 1 + helper(index))
                else:
                    break

            return ans

        maxJumps = 1
        for i in range(len(arr)):
            maxJumps = max(maxJumps, helper(i))

        return maxJumps
