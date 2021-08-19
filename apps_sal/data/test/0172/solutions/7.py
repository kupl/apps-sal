from sys import stdin
from collections import defaultdict
n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
a_d = defaultdict(int)
b_d = defaultdict(int)
for i in range(n):
    a_d[a[i]] += 1
    b_d[b[i]] += 1
f = True
ans = 0
for i in range(6):
    if (a_d[i] + b_d[i]) % 2:
        f = False
        break
    ans += abs(a_d[i] - b_d[i])
if f:
    print(ans // 4)
else:
    print(-1)
