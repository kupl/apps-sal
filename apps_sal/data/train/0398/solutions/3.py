class Solution:

    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        (count, current, solution) = ({0: 1}, 0, 0)
        for num in nums:
            current += num
            solution += count.get(current - k, 0)
            count[current] = count.get(current, 0) + 1
        return solution
