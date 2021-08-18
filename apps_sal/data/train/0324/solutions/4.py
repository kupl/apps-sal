class Solution:
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = list(str(n))
        size = len(nums)
        for i in range(size - 1, -1, -1):
            if nums[i - 1] < nums[i]:
                break
        if i > 0:
            for j in range(size - 1, -1, -1):
                if nums[j] > nums[i - 1]:
                    nums[i - 1], nums[j] = nums[j], nums[i - 1]
                    break
        '''
         230241 230421 230412 要注意的就是这个地方 并不是把4挪到了2的前面就结束了 
         '''
        for k in range((size - i) // 2):
            nums[i + k], nums[size - k - 1] = nums[size - k - 1], nums[i + k]

        ans = int(''.join(nums))
        return n < ans <= 0x7FFFFFFF and ans or -1
