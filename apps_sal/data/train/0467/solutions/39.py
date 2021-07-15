class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def compute(n):
            s = set()
            for i in range(1, 1 + int(n**0.5)):
                if n % i == 0:
                    s.add(i)
                    s.add(n // i)
            return sum(s) if len(s) == 4 else 0
        return sum(compute(i) for i in nums)
