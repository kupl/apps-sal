# Oct 5, while preparing for Microsoft
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        if not arr:
            return 0

        result = [0] * len(arr)

        def _helper(i: int) -> int:
            if result[i]:
                return result[i]

            result[i] = 1

            j = 1
            while j <= d and i + j < len(arr) and arr[i + j] < arr[i]:
                result[i] = max(result[i], _helper(i + j) + 1)
                j += 1

            j = 1
            while j <= d and i - j >= 0 and arr[i - j] < arr[i]:
                result[i] = max(result[i], _helper(i - j) + 1)
                j += 1

            return result[i]

        for i in range(len(arr)):
            _helper(i)

        return max(result)

