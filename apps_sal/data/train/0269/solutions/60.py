class Solution:
    def kLengthApart1(self, nums: List[int], k: int) -> bool:
        d = [i for i, v in enumerate(nums) if v == 1]
        # print(d)
        for i in range(1, len(d)):
            if d[i] - d[i - 1] <= k:
                return False
        return True

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        idx = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                if idx != -1 and i - idx - 1 < k:
                    return False
                idx = i
        return True
