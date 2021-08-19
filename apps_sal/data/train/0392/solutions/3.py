from scipy.special import comb


class Solution:

    def numWays(self, s: str) -> int:
        n = sum((c == '1' for c in s))
        if n % 3:
            return 0
        if n == 0:
            return comb(len(s) - 1, 2, exact=True) % 1000000007
        k = n // 3
        s_iter = iter(s)
        splited = s.split('1')
        return (len(splited[k]) + 1) * (len(splited[2 * k]) + 1) % 1000000007
