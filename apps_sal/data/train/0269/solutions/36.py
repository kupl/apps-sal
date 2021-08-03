class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        ones = [-k - 1]
        for i, num in enumerate(nums):
            if num:
                if i - ones[-1] < k + 1:
                    return False
                else:
                    ones.append(i)
        return True
