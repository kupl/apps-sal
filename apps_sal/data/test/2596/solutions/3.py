from sys import stdin
from bisect import bisect_right as br
input = stdin.readline
(n, k, m, t) = list(map(int, input().split()))
ans = [0] * n
ans[k - 1] = 1
for i in range(t):
    (d, u) = list(map(int, input().split()))
    if d == 0:
        a = ans[:u]
        b = ans[u:]
        if 1 in a:
            print(len(a), a.index(1) + 1)
            ans = a[:]
        else:
            print(len(b), b.index(1) + 1)
            ans = b[:]
    else:
        ans = ans[:u - 1] + [0] + ans[u - 1:]
        print(len(ans), ans.index(1) + 1)
