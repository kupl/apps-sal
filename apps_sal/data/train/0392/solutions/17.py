class Solution:
    def numWays(self, s: str) -> int:
        st = collections.Counter(s)
        n = len(s)
        mod = 10**9 + 7
        if st['1'] == 0:
            return (((n - 1) * (n - 2)) // 2) % mod
        if st['1'] % 3:
            return 0

        x = st['1'] // 3
        i = 0
        count = 0
        b1, b2 = 0, 0
        while count <= 2 * x:
            if s[i] == '1':
                count += 1
                if count == x:
                    b1 += 1
                elif count == 2 * x:
                    b2 += 1
            if s[i] == '0' and count == x:
                b1 += 1

            if s[i] == '0' and count == 2 * x:
                b2 += 1
            i += 1

        return (b1 * b2) % mod
