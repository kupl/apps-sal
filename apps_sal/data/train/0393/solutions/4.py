class Solution:

    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        """
        the fact: num1*num2=LCM*GCD -> LCM=num1*num2//gcd

        """
        ab = a * b // math.gcd(a, b)
        bc = b * c // math.gcd(c, b)
        ac = a * c // math.gcd(a, c)
        abc = ab * c // math.gcd(ab, c)

        def nthUgly(k: int) -> bool:
            h = k // a + k // b + k // c - k // ab - k // ac - k // bc + k // abc
            if h >= n:
                return True
            return False
        (left, right) = (1, 10 ** 10)
        while left < right:
            mid = (right + left) // 2
            if nthUgly(mid):
                right = mid
            else:
                left = mid + 1
        return left
