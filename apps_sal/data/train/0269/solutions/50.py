class Solution:

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last1 = -1
        for num in nums:
            if num == 0 and last1 != -1:
                last1 += 1
            elif num == 1 and last1 != -1:
                if last1 < k:
                    return False
                last1 = 0
            elif num == 1 and last1 == -1:
                last1 = 0
        return True
