class Solution:

    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:

        def isEnough(num):
            total = num // a + num // b + num // c - num // ab - num // ac - num // bc + num // abc
            return total >= n
        ab = a * b // math.gcd(a, b)
        ac = a * c // math.gcd(a, c)
        bc = b * c // math.gcd(b, c)
        abc = a * bc // math.gcd(a, bc)
        left = 1
        right = 10 ** 10
        while left < right:
            mid = left + (right - left) // 2
            if isEnough(mid):
                right = mid
            else:
                left = mid + 1
        return left
