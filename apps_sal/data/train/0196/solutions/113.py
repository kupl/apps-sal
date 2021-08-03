class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        max_sums_left = []
        max_sums_right = collections.deque()
        sum_up_to_index = []
        max_sums_index_right = collections.deque()
        min_sum_right = 0
        min_sum_left = 0
        max_sum_right = 0
        max_sum_left = 0
        sum_left = 0
        sum_right = 0
        ret = -999999999

        for i in range(len(A)):
            sum_left += A[i]
            sum_right += A[-i - 1]
            sum_up_to_index.append(sum_left)
            max_sums_left.append(sum_left - min_sum_left)
            max_sums_right.appendleft(sum_right - min_sum_right)

            if (sum_left < min_sum_left):
                min_sum_left = sum_left

            if (sum_right > max_sum_right):
                max_sums_index_right.appendleft((len(A) - i - 1, sum_right, ))
                max_sum_right = sum_right
            elif (sum_right < min_sum_right):
                min_sum_right = sum_right
            else:
                pass

        sum_left = 0

        for i in range(len(A)):
            if (len(max_sums_index_right) and i == max_sums_index_right[0][0]):
                max_sums_index_right.popleft()

            sum_left += A[i]
            candidates = [max_sums_left[i] + max_sums_right[i] - A[i], sum_right + max_sum_left]
            sum_right -= A[i]

            if (sum_left > max_sum_left):
                max_sum_left = sum_left

            if (len(max_sums_index_right)):
                candidates.append(sum_left + max_sums_index_right[0][1])

            candidate = max(candidates)

            if (candidate > ret):
                ret = candidate

        return ret
