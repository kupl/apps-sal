class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        
        @lru_cache(None)
        def divisors(v):
            res = []
            for i in range(1,ceil(sqrt(v))+2):
                if len(res) > 4: return 0
                if not v % i:
                    res += i,
                    if v//i > i:
                        res += v//i,
                    else:
                        break
            res = set(res)
            return sum(res) if len(res)==4 else 0
        
        for v in nums:
            res += divisors(v)
            
        return res

