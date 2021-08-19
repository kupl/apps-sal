class Solution:

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k > 0:
            flag = False
            last1 = -1
            for i in range(len(nums)):
                if not flag:
                    if nums[i] == 1:
                        flag = True
                        last1 = i
                elif nums[i] == 1:
                    if i - last1 - 1 < k:
                        return False
                    last1 = i
            return True
        else:
            return True
