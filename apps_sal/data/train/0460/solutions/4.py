class Solution:

    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 1
        for i in range(len(nums)):
            count = 1
            if i == nums[i]:
                continue
            index = nums[i]
            nums[i] *= -1
            flag = True
            while flag:
                if index < 0:
                    flag = False
                    continue
                if nums[index] == 0:
                    count += 1
                    tmp = index
                    index = nums[index]
                    nums[tmp] = -20001
                if nums[index] > 0:
                    count += 1
                    tmp = index
                    index = nums[index]
                    nums[tmp] *= -1
                else:
                    if count > longest:
                        longest = count
                    flag = False
        return longest
