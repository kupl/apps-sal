class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        def addToDeqs(min_deq, max_deq, curr, start_i):
                
            while min_deq and min_deq[-1] > curr:
                min_deq.pop()
            min_deq.append(curr)

            while max_deq and max_deq[-1] < curr:
                max_deq.pop()
            max_deq.append(curr)

            while abs(max_deq[0] - min_deq[0]) > limit:
                if max_deq[0] == nums[start_i]:
                    max_deq.pop(0)
                if min_deq[0] == nums[start_i]:
                    min_deq.pop(0)
                start_i += 1

            return start_i

        min_deq = []
        max_deq = []
        longest_subarray = 0
        start_i = 0
        
        for i, n in enumerate(nums):
            start_i = addToDeqs(min_deq, max_deq, n, start_i)
            length_subarray = (i-start_i)+1
            longest_subarray = max(longest_subarray, length_subarray)
        return longest_subarray




