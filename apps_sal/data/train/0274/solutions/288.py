# make every num in nums become right bound for the subarray once, and find the longest subarray.
# i need to know the max and min value in the subarray, so I'll maintain a  minHeap, maxHeap with (value, index), then I can alway cost O(logn) to get the max and min value.
# O(NlogN)
#
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        VALUE, INDEX = 0, 1
        left = 0
        min_h, max_h = [], []
        max_len = 0
        #nums = [8,2,4,7]
        for right, num in enumerate(nums):  # right= 3, left = 2
            heappush(min_h, (num, right))  # max = [(-7,3)(-4,2)(-2,1)]
            heappush(max_h, (-num, right))  # min = [(4,2)(7,3) (8,0)]
            # check whether the current subarray is valid
            # if it is invalid, pop out the extreme value
            while -max_h[0][VALUE] - min_h[0][VALUE] > limit:
                if max_h[0][INDEX] < min_h[0][INDEX]:
                    left = heappop(max_h)[INDEX] + 1
                else:
                    left = heappop(min_h)[INDEX] + 1
                # clean heap
                while min_h[0][INDEX] < left:
                    heappop(min_h)
                while max_h[0][INDEX] < left:
                    heappop(max_h)
            max_len = max(max_len, right - left + 1)  # max_len = 2
        return max_len
