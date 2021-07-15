# @author 

import sys

class BWOWFactor:
    def solve(self):
        s = input()
        n = len(s)
        vv_pre = [0] * (n + 1)
        vv_suf = [0] * (n + 1)

        for i in range(n - 1):
            vv_pre[i + 1] = vv_pre[i]
            if s[i] == s[i + 1] == 'v':
                vv_pre[i + 1] += 1

        for i in range(n - 1, 0, -1):
            vv_suf[i - 1] = vv_suf[i]
            if s[i] == s[i - 1] == 'v':
                vv_suf[i - 1] += 1


        ans = 0
        for i in range(2, n - 2):
            if s[i] == 'o':
                ans += vv_pre[i - 1] * vv_suf[i + 1]

        
        print(ans)

solver = BWOWFactor()
input = sys.stdin.readline

solver.solve()

