class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        dic = {1: -1}
        temp = 1
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                dic = {1: i}
                temp = 1
                continue
            if nums[i] < 0:
                temp = -temp
            if not dic.get(temp) is None:
                res = max(res, i - dic[temp])
            else:
                dic[temp] = i

        return res
