class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        @lru_cache(None)
        def divisors(v):
            res = set()
            for i in range(1,ceil(sqrt(v))+2):
                if not v % i:
                    res.add(i)
                    res.add(v//i)
                if len(res) > 4: return 0
            return sum(res) if len(res)==4 else 0
        return sum(map(divisors, nums))
        

