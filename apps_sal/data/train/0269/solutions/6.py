class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        zCounter = k

        for n in nums:
            if n == 1:
                if zCounter < k:
                    return False
                zCounter = 0
            else:
                zCounter += 1
        return True
