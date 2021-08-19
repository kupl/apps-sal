class Solution:

    def numWays(self, s: str) -> int:
        mod = 10 ** 9 + 7
        c = s.count('1')
        if c % 3 != 0:
            return 0
        if c == 0:
            tot = 0
            for i in range(len(s) - 2):
                tot += len(s) - 2 - i
            return tot % mod
        lsplit = c // 3
        rsplit = lsplit * 2
        (lz, rz) = (1, 1)
        cnt = 0
        for n in s:
            if n == '1':
                cnt += 1
            elif cnt == lsplit:
                lz += 1
            elif cnt == rsplit:
                rz += 1
        return lz * rz % mod
