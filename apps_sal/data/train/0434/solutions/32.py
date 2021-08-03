'''
Using sliding window

Method 1:
Sliding window size shrinks

Use i and j as the lower and upper bounds, both inclusively;
Loop through the nums by upper bound, accumulate current element on the sum, then check if sum is less than j - i (which implies the window includes at least 2 0s) : if yes, keep increase the lower bound i till either the sliding window has at most 1 zero or lower bound is same as upper bound;
Core concept here: - credit to @lionkingeatapple and @abhinav_7.
sum count the number of 1s in the window.
j - i means the length of the window - 1. Since we need to delete one element which is zero from this window, we use j - i not j - i + 1.
Specifically, if

sum == (j - i) + 1
then all 1's exist in the window(i - j); if

sum == (j - i)
one zero exist; if

sum < (j - i)
more than one zeros exist!

TC: O(n)
SC: O(1)
'''


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        i = 0
        j = 0
        sum = 0
        ans = 0

        for j, val in enumerate(nums):
            sum += val
            while(i < j and sum < j - i):
                sum -= nums[i]
                i += 1

            ans = max(ans, j - i)

        return ans
