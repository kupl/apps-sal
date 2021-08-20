class Solution:

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        print(nums)

        def swap(a, i, j):
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

        def helper(index, path):
            if index == len(nums) - 1:
                res.append(path.copy())
            for i in range(index, len(nums)):
                swap(path, index, i)
                helper(index + 1, path.copy())
        helper(0, nums)
        print(nums)
        return res
