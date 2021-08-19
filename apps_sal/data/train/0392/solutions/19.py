from math import factorial


class Solution:

    def numWays(self, s: str) -> int:
        ans = 0
        n = len(s)
        xd = s.count('1')
        if s.count('0') == 0:
            if xd % 3 != 0:
                return 0
            return 1
        if xd == 0:
            if n == 3:
                return 1
            n = n - 1
            ans = factorial(n) / factorial(n - 2) / factorial(2)
        else:
            if xd % 3 != 0:
                return 0
            x = xd // 3
            ti = [x, x]
            j = 0
            while ti[0] > 0:
                if s[j] == '1':
                    ti[0] -= 1
                j += 1
            ti[0] = j
            while ti[1] > 0:
                if s[j] == '1':
                    ti[1] -= 1
                j += 1
            ti[1] = j
            zc = [0, 0]
            j = ti[0]
            while s[j] == '0':
                zc[0] += 1
                j += 1
            j = ti[1]
            while s[j] == '0':
                zc[1] += 1
                j += 1
            lv = 0
            rv = 0
            if zc[0] > 0:
                zc[0] += 1
                lv = factorial(zc[0]) / factorial(zc[0] - 1)
            if zc[1] > 0:
                zc[1] += 1
                rv = factorial(zc[1]) / factorial(zc[1] - 1)
            if max([lv, rv]) == 0:
                return 1
            if lv > 0 and rv > 0:
                ans = lv * rv
            else:
                ans = lv + rv
        ans = int(ans)
        return ans % (10 ** 9 + 7)
