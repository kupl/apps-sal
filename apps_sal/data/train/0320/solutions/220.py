class Solution:
    def minOperations(self, nums: List[int]) -> int:
        inc, mult = 0, 0

        for i in nums:
            if i:
                a, b = self.getRes(i)
                inc += a
                mult = max(mult, b)

        return inc + mult

    def getRes(self, n):
        inc, mult = 0, 0

        while n:
            if n % 2 == 1:
                n -= 1
                inc += 1
            else:
                n //= 2
                mult += 1

        return inc, mult
