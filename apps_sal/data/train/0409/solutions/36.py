class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        if k == 1:
            return self.maxSubArray(arr)
        else:
            arr_sum = sum(arr)

            if arr_sum > 0:
                max_sum = self.maxSubArray(arr) + (k - 1) * arr_sum
                max_sum = max_sum % (10**9 + 7)
                print('pos')
            else:
                max_sum = self.maxSubArray(arr + arr)
                print('neg')

        return max_sum

    def maxSubArray(self, arr):
        curr_sum = 0
        max_sum = 0
        for a in arr:
            curr_sum = max(curr_sum + a, a)
            max_sum = max(max_sum, curr_sum)

        return max_sum
