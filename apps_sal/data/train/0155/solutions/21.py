class Solution:

    def maxJumps(self, arr: List[int], d: int) -> int:
        result = 1
        N = len(arr)
        cache = {}

        def helper(i: int) -> int:
            if i in cache:
                return cache[i]
            result = 1
            if (i == 0 or arr[i] <= arr[i - 1]) and (i == N - 1 or arr[i] <= arr[i + 1]):
                cache[i] = result
                return cache[i]
            j = i - 1
            while j >= 0 and j >= i - d and (arr[j] < arr[i]):
                cur = helper(j)
                result = max(result, cur + 1)
                j = j - 1
            j = i + 1
            while j < N and j <= i + d and (arr[j] < arr[i]):
                cur = helper(j)
                result = max(result, cur + 1)
                j = j + 1
            cache[i] = result
            return cache[i]
        for i in range(N):
            cur = helper(i)
            result = max(cur, result)
        return result
