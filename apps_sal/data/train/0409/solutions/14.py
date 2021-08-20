class Solution:

    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:

        def findMaxSum(arr):
            num_sum = 0
            dp = arr[0]
            max_num = arr[0]
            for i in range(1, len(arr)):
                num = arr[i]
                dp = max(dp + num, num)
                max_num = max(max_num, dp)
            return max_num if max_num >= 0 else 0
        if k == 0:
            return 0
        elif k == 1:
            return findMaxSum(arr)
        elif k == 2 or sum(arr) < 0:
            return findMaxSum(arr + arr)
        else:
            return (sum(arr) * (k - 2) + findMaxSum(arr + arr)) % (10 ** 9 + 7)
