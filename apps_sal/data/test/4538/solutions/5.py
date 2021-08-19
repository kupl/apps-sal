from math import sqrt
(n, d) = map(int, input().split())
cnt = 0
for _ in range(n):
    (p, q) = map(int, input().split())
    if sqrt(p * p + q * q) <= d:
        cnt += 1
print(cnt)
