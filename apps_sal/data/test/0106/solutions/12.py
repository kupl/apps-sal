x = list(map(int, input().split()))
a, b = list(map(int, input().split()))
n = x[0]
m = x[1]
k = x[2]
l1 = 0
p1 = 0
l2 = 0
p2 = 0
t = 0
if a < m * k:
    p1 = 1
else:
    if a % (m * k) == 0:
        p1 = a // (m * k)
    else:
        p1 = a // (m * k) + 1
if (a - (p1 - 1) * m * k) < k:
    l1 = 1
else:
    if (a - (p1 - 1) * m * k) % k == 0:
        l1 = (a - (p1 - 1) * m * k) // k
    else:
        l1 = (a - (p1 - 1) * m * k) // k + 1
if b < m * k:
    p2 = 1
else:
    if b % (m * k) == 0:
        p2 = b // (m * k)
    else:
        p2 = b // (m * k) + 1
if (b - (p2 - 1) * m * k) < k:
    l2 = 1
else:
    if (b - (p2 - 1) * m * k) % k == 0:
        l2 = (b - (p2 - 1) * m * k) // k
    else:
        l2 = (b - (p2 - 1) * m * k) // k + 1
if p1 == p2:
    if l1 == l2:
        t = 0
    else:
        t = min((abs((l1 - l2)) + 10), abs((l1 - l2)) * 5)
else:
    if l1 > 1:
        t = min((l1 - 1) * 5, l1 + 10 - 1)
    else:
        t = 0
    t += 15 * min(abs((p1 - p2)), n - max(p1, p2) + min(p1, p2))
    if l2 > 1:
        t += min((10 + l2 - 1), (l2 - 1) * 5)
print(t)
