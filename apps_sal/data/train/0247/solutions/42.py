# Reference : https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/discuss/685486/JAVA-O(N)-Time-Two-Pass-Solution-using-HashMap.


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:

        # prefix sum
        # in dictionary, store {sum_until_idx: idx}

        # iterate through the array and keep current sum
        # 1. have a left_min_len to track the min length until current idx
        # if current sum + target is in the dictionary,
        # then it means there is a target in the right side of the array
        prefix_sum = {0: -1}
        cur_sum = 0
        for i, val in enumerate(arr):
            cur_sum += val
            prefix_sum[cur_sum] = i

        left_min_len = float('inf')
        ans = float('inf')
        cur_sum = 0
        for i, val in enumerate(arr):
            cur_sum += val
            if (cur_sum - target) in prefix_sum:
                left_min_len = min(left_min_len, i - prefix_sum[cur_sum - target])
            if (cur_sum + target) in prefix_sum:
                ans = min(ans, left_min_len + prefix_sum[cur_sum + target] - i)

        return ans if ans < float('inf') else -1
