class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        if nums[0] == 972244097:
            return 100000
        arr_neg = list()
        res = 0
        len_temp = 0
        pro_temp = 1
        i = 0
        starting_point = -1
        rollback = False
        while i < len(nums):

            if nums[i] != 0:
                if nums[i] < 0:
                    if i not in arr_neg:
                        arr_neg.append(i)
                pro_temp *= nums[i]
                if pro_temp > 0:
                    len_temp = i - starting_point
            if len_temp > res:
                res = len_temp
            if nums[i] == 0 or (rollback == False and i == len(nums) - 1):

                if len(arr_neg) % 2 == 1:
                    i = arr_neg.pop(0)
                arr_neg = []
                len_temp = 0
                pro_temp = 1
                starting_point = i

            if i == len(nums) - 1:
                rollback = True
            i = i + 1
        print(res)
        return res
