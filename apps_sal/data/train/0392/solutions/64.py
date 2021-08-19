def findall(p, s):
    """Yields all the positions of
    the pattern p in the string s."""
    i = s.find(p)
    while i != -1:
        yield i
        i = s.find(p, i + 1)


def choose(n, k):
    c = 1
    if k > n // 2:
        k = n - k
    for i in range(1, k + 1):
        c = c * (n - i + 1) // i
    return c


def modulo(n):
    return n % (10 ** 9 + 7)


class Solution:

    def numWays(self, s: str) -> int:
        n = len(s)
        c = s.count('1')
        if c % 3 != 0:
            return 0
        cp = c // 3
        if cp == 0:
            return modulo(choose(n - 1, 2))
        indices = list(findall('1', s))
        n1 = indices[cp] - indices[cp - 1] - 1
        n2 = indices[cp * 2] - indices[cp * 2 - 1] - 1
        result = 0
        if n1 == 0:
            result = n2 + 1
        elif n2 == 0:
            result = n1 + 1
        else:
            result = (n1 + 1) * (n2 + 1)
        return modulo(result)
