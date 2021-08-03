import itertools


class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        if N == 1:
            return True

        digits = self._getDigits(N)
        ones = {2, 4, 6, 8} & set(digits)
        if not ones:
            return False

        for o in ones:
            digits.remove(o)
            if self._canMakePowerOf2(digits, o):
                return True
            digits.append(o)
        return False

    def _getDigits(self, N):
        digits = []
        while N > 0:
            digits.append(N % 10)
            N //= 10
        return digits

    def _canMakePowerOf2(self, digits, ones):
        for seq in itertools.permutations(digits):
            if self._isPowerOf2(seq, ones):
                return True
        return False

    def _isPowerOf2(self, digits, ones):
        n = 0
        for i, d in enumerate(digits):
            if i == 0 and d == 0:
                return False
            n = 10 * n + d
        n = 10 * n + ones
        return n & (n - 1) == 0
