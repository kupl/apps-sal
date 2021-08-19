class Solution:

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count = 0
        first = False
        for i in nums:
            if i == 1 and (not first):
                first = True
            elif i == 1 and first:
                if k <= count:
                    count = 0
                else:
                    return False
            else:
                count += 1
        return True
