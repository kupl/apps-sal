

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        '''
        the fact: num1*num2=LCM*GCD -> LCM=num1*num2//gcd

        '''
        ab = a * b // math.gcd(a, b)
        ac = a * c // math.gcd(a, c)
        bc = b * c // math.gcd(b, c)
        abc = ab * c // math.gcd(ab, c)

        def has_nsmaller(num):
            k = num // a + num // b + num // c - num // ac - num // ab - num // bc + num // abc
            return k >= n

        low, high = 0, 2 * 10**9
        while low < high:
            mid = (low + high) // 2
            if has_nsmaller(mid):
                high = mid
            else:
                low = mid + 1
        return low
