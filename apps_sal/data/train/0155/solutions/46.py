class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        @lru_cache(None)
        def jump(mid):
            left = max(mid - d, 0)
            right = min(mid + d, len(arr) - 1)

            res = 1
            for i in range(mid - 1, left - 1, -1):
                if arr[i] >= arr[mid]:
                    break
                res = max(res, jump(i) + 1)
            for i in range(mid + 1, right + 1):
                if arr[i] >= arr[mid]:
                    break
                res = max(res, jump(i) + 1)
            return res

        res = [1] * len(arr)
        for i in range(len(arr)):
            res[i] = jump(i)
        return max(res)
