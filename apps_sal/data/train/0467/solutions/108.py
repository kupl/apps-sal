class Solution:

    def sumFourDivisors(self, nums: List[int]) -> int:
        return sum([self.sumofDivisors(num) for num in nums])

    def sumofDivisors(self, num):
        s = set()
        for i in range(1, int(sqrt(num)) + 1):
            if num % i == 0:
                s.add(i)
                s.add(num // i)
            if len(s) > 4:
                return 0
        return sum(s) if len(s) == 4 else 0
