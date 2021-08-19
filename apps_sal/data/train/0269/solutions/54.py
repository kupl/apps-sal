class Solution:

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = 0
        i = 0
        for num in nums:
            if num == 1:
                if prev and k > i - prev:
                    return False
                prev = i + 1
            i += 1
        return True
