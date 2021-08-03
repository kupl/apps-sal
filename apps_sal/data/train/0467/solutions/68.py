class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans = 0
        for n in nums:
            rangemax = int(math.sqrt(n))
            factsum = n + 1
            factcount = 2
            for f1 in range(2, rangemax + 1):
                if not n % f1:
                    f2 = n // f1
                    factcount += 1
                    factsum += f1
                    if f1 != f2:
                        factcount += 1
                        factsum += f2
                    if factcount > 4 or factcount % 2:
                        break
            if factcount == 4:
                ans += factsum
        return ans
