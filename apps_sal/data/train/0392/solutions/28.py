class Solution:
    def numWays(self, s: str) -> int:
        mod = pow(10, 9) + 7
        cnt = s.count('1')
        if cnt == 0:
            return (len(s) - 1) * (len(s) - 2) // 2 % mod
        if cnt % 3 != 0:
            return 0
        ones = []
        for i, x in enumerate(s):
            if x == '1':
                ones.append(i)
        return (ones[cnt // 3] - ones[cnt // 3 - 1]) * (ones[2 * cnt // 3] - ones[2 * cnt // 3 - 1]) % mod
