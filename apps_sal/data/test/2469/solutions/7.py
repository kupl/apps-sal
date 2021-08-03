class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        res = []
        n = len(nums)
        for i in range(n):
            dic[nums[i]] = dic.get(nums[i], 0) + 1
        print(dic)
        for num, cnt in dic.items():
            if cnt > n / 3:
                res.append(num)
        return res
