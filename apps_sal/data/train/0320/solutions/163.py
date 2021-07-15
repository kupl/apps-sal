def ones(x):
    return 0 if x == 0 else 1 + ones(x & (x - 1))
def twos(x):
    cc = 0
    while x > 1:
        x //= 2
        cc += 1
    return cc

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        o = 0
        t = 0
        for x in nums:
            o += ones(x)
            t = max(t, twos(x))
        return o + t
