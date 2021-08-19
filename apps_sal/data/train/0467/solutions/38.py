class Solution:
    cache = {}

    def factors(self, n):
        if n in self.cache:
            return self.cache[n]
        result = set()
        for i in range(1, int(n ** 0.5) + 1):
            (div, mod) = divmod(n, i)
            if mod == 0:
                result |= {i, div}
        self.cache[n] = result
        return result

    def sumFourDivisors(self, nums: List[int]) -> int:
        factors = [self.factors(f) for f in nums]
        return sum([sum(f) for f in factors if len(f) == 4])
