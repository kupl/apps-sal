class Solution:

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = 0
        s = set(nums)
        for i in nums:
            cnt = 1
            tmp = i - 1
            while tmp in s:
                cnt += 1
                s.discard(tmp)
                tmp -= 1
            tmp = i + 1
            while tmp in s:
                cnt += 1
                s.discard(tmp)
                tmp += 1
            max_count = max(max_count, cnt)
        return max_count
