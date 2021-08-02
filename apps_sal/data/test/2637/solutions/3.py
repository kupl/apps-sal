class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()

        def swap(a, i, j):
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

        def helper(index, path):
            if index == len(nums) - 1:
                res.append(path.copy())
            for i in range(index, len(nums)):
                if i != index and path[i] == path[index]:
                    continue
                swap(path, index, i)
                helper(index + 1, path.copy())

        helper(0, nums)
        return res
