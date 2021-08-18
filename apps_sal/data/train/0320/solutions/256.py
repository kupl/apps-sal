class Solution:
    def minOperations(self, nums: List[int]) -> int:
        lru_cache(maxsize=None)

        def check(n):
            if n == 0:
                return (0, 0)
            elif n == 1:
                return (1, 0)
            else:
                r1 = 0
                r2 = 0

                k, l = divmod(n, 2)
                r1, r2 = check(k)
                r1 += l
                r2 += 1
            return r1, r2

        r1 = 0
        r2 = 0
        for n in nums:
            c1, c2 = check(n)
            r1 += c1
            r2 = max(r2, c2)

        return r1 + r2
