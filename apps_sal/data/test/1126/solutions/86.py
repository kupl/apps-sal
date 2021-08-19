from collections import deque
(n, x, m) = map(int, input().split())
A = deque()
G = [-1 for i in range(m)]
t = 0
total = 0
while G[x] == -1:
    A.append(x)
    G[x] = t
    t += 1
    total += x
    x = x * x % m
cycle = t - G[x]
s = 0
for i in range(cycle):
    s += A[G[x] + i]
ans = 0
if n < t:
    for i in range(n):
        ans += A[i]
else:
    n -= t
    ans = total + s * (n // cycle)
    for i in range(n % cycle):
        ans += A[G[x] + i]
print(ans)
