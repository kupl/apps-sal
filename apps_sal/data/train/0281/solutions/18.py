import string


class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False

        mod = k % 26
        div = k // 26

        def f(sh):
            l = 1 if sh < mod else 0
            return div + l

        shifts = [0 for i in range(26)]
        for l1, l2 in zip(s, t):
            if l1 == l2:
                continue
            sh = string.ascii_lowercase.index(l2) - string.ascii_lowercase.index(l1)
            sh = sh if sh >= 0 else sh + 26
            shifts[sh - 1] += 1
            if shifts[sh - 1] > f(sh - 1):
                return False

        return True
