class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def check(x):
            v = set()
            i = 1
            while i * i <= x:
                if x % i == 0:
                    v.add(i)
                    v.add(x // i)
                    if len(v) > 4:
                        return 0
                i += 1
            if len(v) == 4:
                return sum(v)
            return 0
        return sum([check(x) for x in nums])

