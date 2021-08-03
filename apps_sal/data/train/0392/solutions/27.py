class Solution:
    def numWays(self, s: str) -> int:
        n = len(s)
        n1 = s.count('1')
        if n1 % 3 != 0:
            return 0
        if n1 == 0:
            return int((n - 2) * (n - 1) / 2) % 1000000007
        j = 0
        k = 0
        l = 0
        m = 0
        counter1 = 0
        for i in range(0, n):
            if s[i] == '1':
                counter1 += 1
                if counter1 == n1 / 3:
                    j = i
                if counter1 == n1 / 3 + 1:
                    k = i
                if counter1 == n1 / 3 * 2:
                    l = i
                if counter1 == n1 / 3 * 2 + 1:
                    m = i
                    break
        return (k - j) * (m - l) % 1000000007
