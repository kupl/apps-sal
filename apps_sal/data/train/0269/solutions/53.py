class Solution:

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        distance = k
        for num in nums:
            if num:
                if distance < k:
                    return False
                distance = 0
            else:
                distance = distance + 1
        return True
