class Solution:

    def find_factors(self, n):
        factors = []
        i = 1
        j = n
        while True:
            if i * j == n:
                factors.append(i)
                if i == j:
                    break
                factors.append(j)
            i += 1
            j = n // i
            if i > j:
                break
        return factors

    def sumFourDivisors(self, nums: List[int]) -> int:
        d = 0
        for i in nums:
            f = self.find_factors(i)
            if len(f) == 4:
                d += f[0] + f[1] + f[2] + f[3]
        return d
