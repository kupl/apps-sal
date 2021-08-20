import time
(n, m) = (int(i) for i in input().split())
a = [int(i) for i in input().split()]
start = time.time()
d = {}
ans = 0
for i in range(m):
    d[i] = 0
for i in a:
    d[i - 1] += 1
k = n
for i in range(m - 1):
    k -= d[i]
    ans += d[i] * k
print(ans)
finish = time.time()
