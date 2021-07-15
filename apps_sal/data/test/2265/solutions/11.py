# @author 

import sys

class CVusTheCossackAndStrings:
    def solve(self):
        a = input().strip()
        b = input().strip()
        n = len(a)
        m = len(b)
        oa = 0
        ob = b.count('1')
        ans = 0
        for i in range(n):
            if a[i] == '1':
                oa += 1
            if i == m - 1:
                if abs(oa - ob) % 2 == 0:
                    ans += 1
            elif i >= m:
                if a[i - m] == '1':
                    oa -= 1
                if abs(oa - ob) % 2 == 0:
                    ans += 1
                    

        print(ans)

solver = CVusTheCossackAndStrings()
input = sys.stdin.readline

solver.solve()

