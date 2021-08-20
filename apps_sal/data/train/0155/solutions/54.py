class Solution:

    def maxJumps(self, arr: List[int], d: int) -> int:
        from functools import lru_cache
        n = len(arr)

        @lru_cache(maxsize=None)
        def f(i):
            res = 1
            for j in range(i + 1, min(i + d + 1, n)):
                if arr[j] < arr[i]:
                    res = max(res, 1 + f(j))
                else:
                    break
            for j in range(i - 1, max(-1, i - d - 1), -1):
                if arr[j] < arr[i]:
                    res = max(res, 1 + f(j))
                else:
                    break
            return res
        return max((f(_) for _ in range(n)))
