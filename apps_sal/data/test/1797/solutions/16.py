n = int(input())
p = [int(x) for x in input().split()]
p.insert(0, -3)
max1, max2 = 0, 0
used = [0] * (n + 1)
count = 0
for i in range(1, n + 1):
    m = 0
    v = i
    while used[p[v]] == 0:
        used[p[v]] = 1
        v = p[v]
        m += 1
    if m > max2:
        max2 = m
    if max2 > max1:
        max2, max1 = max1, max2
    count += m**2
count = count - max1**2 - max2**2 + (max1 + max2)**2

print(count)
