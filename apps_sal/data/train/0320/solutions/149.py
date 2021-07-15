class Solution:
    def minOperations(self, nums: List[int]) -> int:
        one = 0
        two = 0
        for n in nums:
            r = self.onetwo(n)
            one += r[0]
            two = max(two, r[1])
        return one + two
    def onetwo(self, n):
        one = 0
        two = 0
        while n != 0:
            if n%2 == 0:
                two += 1
                n /= 2
            else:
                one += 1
                n -= 1
        return (one, two)
