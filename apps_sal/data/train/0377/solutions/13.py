class Solution:
    def _lcm(self, a, b):
        return a * b // math.gcd(a, b)

    def _nth_magical_number_slow(self, n: int, a: int, b: int) -> int:
        if n == 0:
            return 0
        else:
            i, j = a, b
            count = 1
            while count < n:
                if i <= j:
                    i = i + a
                else:
                    j = j + b

                if i == j:
                    if a < b:
                        i = i + a
                    else:
                        j = j + b

                count += 1

            return min(i, j)

    def nthMagicalNumber(self, n: int, a_orig: int, b_orig: int) -> int:
        a, b = min(a_orig, b_orig), max(a_orig, b_orig)
        if a == b:
            return a * n % 1000000007
        else:
            lcm = self._lcm(a, b)
            k = lcm // a + lcm // b - 1
            return ((n // k) * lcm + self._nth_magical_number_slow(n % k, a, b)) % 1000000007
