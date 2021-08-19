class Solution:
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = list(str(n))  # 因为只有你变成字符串 才可以被分开这样子写
        size = len(nums)
        for i in range(size - 1, -1, -1):
            if nums[i - 1] < nums[i]:
                break
        if i > 0:  # 没有明白这儿为什么需要一个这个判断条件呢
            for j in range(size - 1, -1, -1):
                if nums[j] > nums[i - 1]:
                    nums[i - 1], nums[j] = nums[j], nums[i - 1]
                    break
        # 上面这儿算是比较明白了
        for k in range((size - i) // 2):
            nums[i + k], nums[size - k - 1] = nums[size - k - 1], nums[i + k]
            # 这一步想明白一点
        ans = int(''.join(nums))
        return n < ans <= 0x7FFFFFFF and ans or -1  # 这儿实在是没看懂 神马意思
        # 注意这个地方 虽然都是表示无穷大 但是这个是0x7FFFFFFF 不能用float('inf') 是不是因为这个是浮点型的 有可能
