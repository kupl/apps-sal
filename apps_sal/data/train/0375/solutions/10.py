class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0

        m = 0
        for num in nums:
            m = max(m, num)

        exp = 1
        while m // exp:
            aux = [[] for i in range(10)]
            for num in nums:
                aux[(num // exp) % 10].append(num)
            index = 0
            for item in aux:
                if len(item) != 0:
                    for i in item:
                        nums[index] = i
                        index += 1
            exp *= 10

        maxGap = 0
        pre = nums[0]
        for num in nums:
            maxGap = max(maxGap, num - pre)
            pre = num
        return maxGap
