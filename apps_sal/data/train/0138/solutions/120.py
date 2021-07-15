class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        non_zero_list = []
        neg_list = []
        temp = []
        neg = 0
        for i in range(len(nums)):
            #temp = []
            if nums[i] == 0 or (i == len(nums) - 1):
                if nums[i] != 0:
                    temp.append(nums[i])
                non_zero_list.append(temp)
                temp = []
                if nums[i] < 0:
                    neg += 1
                neg_list.append(neg)
                neg = 0                                
            elif nums[i] < 0:
                neg += 1
                temp.append(nums[i])
            elif nums[i] > 0:
                temp.append(nums[i])
        _max  = 0

        for i in range(len(non_zero_list)):
            if neg_list[i] % 2 == 0:
                if len(non_zero_list[i]) > _max:
                    _max = len(non_zero_list[i])
            else:
                temp1 = 0
                temp2 = 0
                for j in range(len(non_zero_list[i])):
                    if non_zero_list[i][j] < 0:
                        temp1 =len(non_zero_list[i]) - j - 1
                        #print(j, temp1)
                        temp1 = max(temp1, j)
                        break
                for j in range(len(non_zero_list[i])-1, -1, -1):
                     if non_zero_list[i][j] < 0:
                        temp2 =len(non_zero_list[i]) - j - 1
                        #print(j,temp2)
                        temp2 = max(temp2, j )
                        break
                if max(temp1, temp2) > _max:
                    _max = max(temp1,temp2)
        return _max

