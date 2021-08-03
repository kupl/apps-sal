class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            d = set()
            for cnd in range(1, floor(sqrt(n)) + 1):
                q, r = divmod(n, cnd)
                if not r:
                    d.add(q)
                    d.add(cnd)
            if len(d) == 4:
                ans += sum(d)
        return ans
