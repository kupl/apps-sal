class Solution:

    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        ints = []
        while i < len(nums):
            start = i
            end = i
            while i < len(nums) and nums[i] == 1:
                i += 1
                end += 1
            if start != end:
                ints.append((start, end))
            i += 1
        if len(ints) == 1:
            diff = ints[0][1] - ints[0][0]
            if diff == len(nums):
                return diff - 1
            else:
                return diff
        elif not ints:
            return 0
        max_ones = 0
        for seq in range(len(ints) - 1):
            seq1 = ints[seq]
            seq2 = ints[seq + 1]
            length = None
            if seq2[0] - seq1[1] == 1:
                length = seq1[1] - seq1[0] + (seq2[1] - seq2[0])
            else:
                length = max(seq1[1] - seq1[0], seq2[1] - seq2[0])
            if length > max_ones:
                max_ones = length
        return max_ones
