# 1493. Longest Subarray of 1's After Deleting One Element

def get_longest (nums):
    arr = [1-x for x in nums]
    l, r = 0, 0
    count = 0
    max_length = 0
    while l < len (arr):
        if r == len (arr): step = 'l'
        elif l == r: step = 'r'
        elif count + arr[r] > 1: step = 'l'
        else: step = 'r'

        if step == 'l':
            count -= arr[l]
            l += 1
        else:
            count += arr[r]
            r += 1
            max_length = max (max_length, r - l)

    return max (0, max_length - 1)


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        return get_longest(nums)
