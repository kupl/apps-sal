class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            sq = floor(n**0.5)
            if sq * sq == n:
                continue
            divs = 2
            divsum = 1 + n
            for i in range(sq, 1, -1):
                if n % i == 0:
                    divs += 2
                    divsum += i + n // i
                if divs > 4:
                    break
            if divs == 4:
                ans += divsum
        return ans
