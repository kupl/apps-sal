from decimal import Decimal
(n, k) = map(int, input().split())
a = list(map(int, input().split()))
d = [0 for i in range(n)]
d[0] = a[0]
for i in range(1, n):
    d[i] = a[i] + d[i - 1]
cnt = 0
sm = 0
for i in range(k - 1, n):
    cnt += 1
    if i == k - 1:
        sm += d[i]
    else:
        sm += d[i] - d[i - k]
summa = Decimal(sm)
count = Decimal(cnt)
print(summa / count)
