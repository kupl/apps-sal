import math
(h, m) = list(map(int, input().split()))
(H, D, C, N) = list(map(int, input().split()))
mn = (20 - h) * 60 - m
if mn < 0:
    mn = 0
a1 = C * math.ceil(H / N)
a2 = C * 0.8 * math.ceil((H + mn * D) / N)
print(min(a1, a2))
