class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        # p1 * p2
        # 1, p1, p2, p1 * p2
        # p^n: n+1
        # 8: 1, 2, 4, 8
        # p^3
        
        def find_divisors(n):
            i = 1
            divisors = []
            while i * i < n:
                if n % i == 0:
                    divisors.append(i)
                    divisors.append(n // i)
                i += 1
            if i * i == n:
                divisors.append(i)
            return divisors
        
        ans = 0
        for n in nums:
            divisors = find_divisors(n)
            if len(divisors) == 4:
                ans += sum(divisors)
        return ans
