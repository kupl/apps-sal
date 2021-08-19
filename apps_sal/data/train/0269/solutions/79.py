class Solution:

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return True
        flag = 0
        start = 0
        for i in range(len(nums)):
            if i == 0:
                if nums[i] == 1:
                    start = 1
                else:
                    start = 0
                continue
            if nums[i] == 0 and start == 1:
                flag += 1
            if nums[i] == 1:
                if start == 1:
                    if flag < k:
                        return False
                start = 1
                flag = 0
        return True
