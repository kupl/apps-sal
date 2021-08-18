class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        odd = 0
        flag = True
        while len(nums) > 0:
            temp = []
            if flag:
                for x in nums:
                    if x & 1 == 1:
                        res += 1
                        if x - 1 != 0:
                            temp.append(x - 1)
                    elif x != 0:
                        temp.append(x)
                flag = False
            else:
                for x in nums:
                    temp.append(x // 2)
                res += 1
                flag = True
            nums = temp
        return res
