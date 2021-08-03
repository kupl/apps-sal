class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        def less(digits, d):
            return len([i for i in digits if i < d])

        cnt = 0
        ld, ln = len(digits), len(str(n))
        N = str(n)
        for i in range(ln - 1):
            cnt += ld ** (i + 1)
        for i in range(ln):
            cnt += less(digits, N[i]) * (ld ** (ln - i - 1))
            if N[i] not in digits:
                return cnt
        return cnt + 1
