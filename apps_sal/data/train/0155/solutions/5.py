class Solution:

    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        cache = {}

        def find_max_jumps(i):
            if i in cache:
                return cache[i]
            max_jumps = 1
            for dr in [1, -1]:
                for r in range(1, d + 1):
                    if not (0 <= i + dr * r < n and arr[i + dr * r] < arr[i]):
                        break
                    max_jumps = max(max_jumps, 1 + find_max_jumps(i + dr * r))
            cache[i] = max_jumps
            return max_jumps
        result = 1
        for i in range(n):
            result = max(result, find_max_jumps(i))
        return result


class Solution111:

    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        res = [0] * n

        def dp(i):
            if res[i]:
                return res[i]
            res[i] = 1
            for di in [-1, 1]:
                for j in range(i + di, i + di + d * di, di):
                    if not (0 <= j < n and arr[j] < arr[i]):
                        break
                    res[i] = max(res[i], dp(j) + 1)
            return res[i]
        return max(map(dp, range(n)))
