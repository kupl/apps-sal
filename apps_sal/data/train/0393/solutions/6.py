import math


class Solution:

    def ugly(self, n, a, b, c, ab, ac, bc, abc, num):
        return num // a + num // b + num // c - num // ab - num // ac - num // bc + num // abc >= n

    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        left = min(a, b, c)
        right = a * b * c * n
        ab = a * b // math.gcd(a, b)
        ac = a * c // math.gcd(a, c)
        bc = b * c // math.gcd(b, c)
        abc = a * bc // math.gcd(a, bc)
        while left < right:
            mid = left + (right - left) // 2
            if self.ugly(n, a, b, c, ab, ac, bc, abc, mid):
                right = mid
            else:
                left = mid + 1
        return left
