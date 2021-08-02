
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

D = defaultdict(int)
for a in A:
    D[a] += 1

ans = 0
for a, x in D.items():
    if x >= a:
        ans += x - a
    else:
        ans += x

print(ans)
