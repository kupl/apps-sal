import sys
import os

n, k = map(int, input().split())
data = list(map(int, input().split()))
res = 0
resu = 0
for i in range(n):
    res += data[i]
    r = min(res, 8)
    res -= r
    resu += r
    if resu >= k:
        print(i + 1)
        return
        sys.exit
        os.abort()
print(-1)
