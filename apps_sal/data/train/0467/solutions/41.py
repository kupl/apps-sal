class Solution:

    def sumFourDivisors(self, lst: List[int]) -> int:
        import math
        final = 0
        for i in lst:
            factors = []
            for j in range(1, round(math.sqrt(i)) + 1):
                if i % j == 0:
                    factors.append(int(j))
                    factors.append(int(i / j))
            factors = list(dict.fromkeys(factors))
            if len(factors) == 4:
                final += sum(factors)
        return final
