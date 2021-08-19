class Solution:

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count = k
        for num in nums:
            if not num:
                count += 1
            elif count < k:
                return False
            else:
                count = 0
        return True
