class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        counter = 0
        bool = False
        for i in nums:
            if i == 1 and not bool:
                bool = True
            elif i == 1 and counter < k and bool:
                return False
            elif i == 1 and counter >= k and bool:
                counter = 0
            else:
                counter += 1
        return True
