class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        ns = str(n)
        dp = 1
        digits.sort()
        M, N = len(ns), len(digits)

        for i in range(M - 1, -1, -1):
            dp2 = 0

            for d in digits:
                if d > ns[i]:
                    break
                if d < ns[i]:
                    dp2 += N**(M - 1 - i)
                else:
                    dp2 += dp

            dp = dp2
        return dp + sum(N**i for i in range(1, M))
