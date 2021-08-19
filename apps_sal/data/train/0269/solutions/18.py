class Solution:

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        flag = 0
        start = None
        end = 0
        for i in range(len(nums)):
            if nums[i] == 1 and flag == 0:
                start = i
                flag = 1
            elif nums[i] == 1 and flag == 1:
                end = i
                dis = end - start
                start = i
                if dis <= k:
                    return False
        return True
