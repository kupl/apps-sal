class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        i, j = 0, 0
        flag = True
        count = 0
        while i < len(nums):
            if nums[i] == 1:
                if flag:
                    count = 0
                    flag = False
                else:
                    if count < k:
                        return False
                    count = 0
            else:
                count += 1
            i += 1
        return True
