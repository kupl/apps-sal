
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ttl = 0

        for n in nums:
            seen = set()
            for i in range(1, int(sqrt(n)) + 1):
                if n % i == 0:
                    seen.add(i)
                    seen.add(n / i)
                if len(seen) >= 5:
                    break
            if len(seen) == 4:
                ttl += sum(seen)
        return int(ttl)
