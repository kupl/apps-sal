"""
Author: Q.E.D
Time: 2020-09-06 09:39:09
"""
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    quota = 0
    for x in a:
        k = abs(x)
        if x >= 0:
            quota += k
        else:
            r = max(0, k - quota)
            quota -= (k - r)
            ans += r
    print(ans)
