class Solution:

    def makeHalf(self, a):
        for i in range(len(a)):
            a[i] //= 2

    def makeEven(self, a):
        c = 0
        for i in range(len(a)):
            if a[i] % 2 == 0:
                continue
            else:
                a[i] -= 1
                c += 1
        return c

    def minOperations(self, nums: List[int]) -> int:
        op = 0
        while sum(nums) != 0:
            op += self.makeEven(nums)
            if sum(nums) == 0:
                return op
            self.makeHalf(nums)
            op += 1
        return op
