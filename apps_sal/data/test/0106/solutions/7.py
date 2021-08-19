import math
(n, m, k) = list(map(int, input().split()))
(a, b) = list(map(int, input().split()))
p1 = math.ceil(a / (m * k))
e1 = math.ceil((a - (p1 - 1) * (m * k)) / k)
if e1 == 0:
    e1 = m
p2 = math.ceil(b / (m * k))
e2 = math.ceil((b - (p2 - 1) * (m * k)) / k)
if e2 == 0:
    e2 = m
ans = 0
if p1 == p2:
    ans = min(abs(e1 - e2) + 10, abs(e1 - e2) * 5)
else:
    ans = min(e1 - 1 + 10, (e1 - 1) * 5) + min((p1 - p2) % n, (p2 - p1) % n) * 15 + min(e2 - 1 + 10, (e2 - 1) * 5)
print(ans)
