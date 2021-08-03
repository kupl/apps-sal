class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        # https://en.wikipedia.org/wiki/Maximum_subarray_problem
        # Key:
        # Kadane(arr * 2) is always >= Kadane(arr)
        # Kadane(arr * 2) will always cross the boundary if sum(arr) > 0
        # if Kadane(arr * 2) does not cross the boundary, then Kadane(arr * 2) == Kadane(arr)
        def Kadane(arr):
            # Kadane: status machine
            ans, cur = 0, 0
            for num in arr:
                cur = max(cur + num, num)
                ans = max(ans, cur)
            return ans
        return (((k - 2) * max(sum(arr), 0) + Kadane(arr * 2)) if k > 1 else Kadane(arr)) % (10 ** 9 + 7)
