class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        @lru_cache(None)
        def dfs(index):
            res = 0

            for direction in [-1, 1]:
                for jump in range(1, d + 1):
                    j = index + direction * jump
                    if 0 <= j < len(arr) and arr[index] > arr[j]:
                        res = max(res, dfs(j))
                    else:
                        break

            return res + 1

        return max(dfs(i) for i in range(len(arr)))
