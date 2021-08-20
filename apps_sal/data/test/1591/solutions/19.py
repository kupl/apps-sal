import time
(n, k) = (int(i) for i in input().split())
start = time.time()
b = [0 for i in range(k)]
for i in range(n):
    now = int(input()) - 1
    b[now] += 1
ost = 0
ans = 0
for i in range(k):
    d = b[i] % 2
    ans += b[i] - d
    ost += d
ans += ost // 2 + ost % 2
print(ans)
finish = time.time()
