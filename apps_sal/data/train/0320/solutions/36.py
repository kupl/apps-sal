class Solution:

    def minOperations(self, nums: List[int]) -> int:
        totOddRem = 0
        max2Power = 0
        for x in nums:
            pow2 = 0
            while True:
                totOddRem += x & 1
                if x > 1:
                    pow2 += 1
                    x >>= 1
                else:
                    break
            max2Power = max(max2Power, pow2)
        return totOddRem + max2Power
