class Solution:
    def findMaxSubarray(arr):
        counter = 0
        best = 0
        for a in arr:
            counter += a
            if counter < 0:
                counter = 0
            else:
                best = max(best, counter)
        return best

    def maxFromLeft(arr):
        max_from_left = 0
        sum_from_left = 0
        for a in arr:
            sum_from_left += a
            max_from_left = max(max_from_left, sum_from_left)
        return max_from_left

    def maxFromRight(arr):
        max_from_right = 0
        sum_from_right = 0
        for a in reversed(arr):
            sum_from_right += a
            max_from_right = max(max_from_right, sum_from_right)
        return max_from_right

    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        no_reps = Solution.findMaxSubarray(arr)
        if k == 1:
            return no_reps

        arr_sum = sum(arr)
        best_from_left = Solution.maxFromLeft(arr)
        best_from_right = Solution.maxFromRight(arr)

        right_and_left = best_from_right + best_from_left

        right_and_k_and_left = best_from_right + (k - 2) * arr_sum + best_from_left

        res = max(no_reps, right_and_left, right_and_k_and_left)

        return res % (10 ** 9 + 7)
