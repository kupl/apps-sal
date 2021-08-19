class Solution:

    def minOperations(self, nums: List[int]) -> int:

        def calcOps(num):
            one = 0
            two = 0
            while num > 0:
                if num % 2 == 0:
                    num //= 2
                    two += 1
                else:
                    num -= 1
                    one += 1
            return [one, two]
        one = 0
        two = 0
        for x in nums:
            ops = calcOps(x)
            one += ops[0]
            two = max(two, ops[1])
        return one + two
