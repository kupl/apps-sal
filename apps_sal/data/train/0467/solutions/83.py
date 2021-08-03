class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        @lru_cache(None)
        def divisors(v):
            res = set()
            for i in range(1, ceil(sqrt(v)) + 1):
                if not v % i:
                    res.update({i, v // i})
                if len(res) > 4:
                    return 0
            return sum(res) if len(res) == 4 else 0
        return sum(list(map(divisors, nums)))
