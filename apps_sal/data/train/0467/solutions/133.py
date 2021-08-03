class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        import math
        s = 0
        nums = sorted(nums, reverse=True)
        for i in nums:
            count = set()
            true = True
            for x in range(2, int(math.sqrt(i)) + 1):
                if len(count) > 4:
                    true = False
                    break
                if i % x == 0:
                    count.add(x)
                    count.add(i // x)
            if len(count) == 2 and true:
                s += sum(count) + i + 1
        return s
