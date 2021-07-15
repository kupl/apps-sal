class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        counter = -1
        for i in nums:
            if counter < 0:
                if i == 1:
                    counter = 0
            else:
                if i == 0:
                    counter += 1
                else:
                    if counter < k:
                        return False
                    counter = 0
        return True
