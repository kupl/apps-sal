class Solution:

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        counter = -1
        for num in nums:
            if num == 1:
                if counter == -1:
                    counter = 0
                elif counter >= k:
                    counter = 0
                else:
                    return False
            elif counter != -1:
                counter += 1
        return True
    (0, 1, 0, 1)
