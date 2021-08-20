(x, y, l, r) = [int(x) for x in input().split()]
p_x = [1]
p_y = [1]
for i in range(1, 61):
    p_x.append(p_x[len(p_x) - 1] * x)
    p_y.append(p_y[len(p_y) - 1] * y)
possible = set([0])
for i in range(61):
    for j in range(61):
        possible.add(p_x[i] + p_y[j])
a = []
for x in possible:
    a.append(x)
a.sort()
ans = 0
for i in range(1, len(a)):
    l1 = max(a[i - 1], l - 1)
    r1 = min(a[i], r + 1)
    ans = max(ans, r1 - l1 - 1)
print(ans)
