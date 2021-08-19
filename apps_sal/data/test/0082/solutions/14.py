import math
(n, k) = map(int, input().split())
sm = sum(list(map(int, input().split())))
a = 0
while int((sm + a * k) / (n + a) + 0.5) < k:
    a += 1
print(a)
