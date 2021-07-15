import sys
from array import array

n, m, k = list(map(int, input().split()))
block = list(map(int, input().split()))
a = [0] + list(map(int, input().split()))

if block and block[0] == 0:
    print(-1)
    return

prev = array('i', list(range(n)))
for x in block:
    prev[x] = -1

for i in range(1, n):
    if prev[i] == -1:
        prev[i] = prev[i-1]

inf = ans = 10**18

for i in range(1, k+1):
    s = 0
    cost = 0
    while True:
        cost += a[i]
        t = s+i

        if t >= n:
            break
        if prev[t] == s:
            cost = inf
            break
        s = prev[t]

    ans = min(ans, cost)

print(ans if ans < inf else -1)

