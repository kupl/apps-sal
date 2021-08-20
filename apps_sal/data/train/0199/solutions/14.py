class Solution:

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        elms = set()
        visited = set()
        max_consecutive = 0
        for num in nums:
            elms.add(num)
        for num in nums:
            if num in visited:
                continue
            visited.add(num)
            curr_consecutive = 1
            tmp = num - 1
            while tmp in elms:
                visited.add(tmp)
                curr_consecutive += 1
                tmp -= 1
            tmp = num + 1
            while tmp in elms:
                visited.add(tmp)
                curr_consecutive += 1
                tmp += 1
            if curr_consecutive > max_consecutive:
                max_consecutive = curr_consecutive
        return max_consecutive
