(n, c) = map(int, input().split())
x = [0] * n
v = [0] * n
for i in range(n):
    (x[i], v[i]) = map(int, input().split())
x1 = [0] + x
v1 = [0] + v
x2 = [0] + list(map(lambda a: c - a, x[::-1]))
v2 = [0] + v[::-1]
lst1 = [0] * (n + 1)
lst2 = [0] * (n + 1)
lst1[0] = lst2[0] = (0, 0)


def f(l, x, v):
    maxcal = pos = sumcal = 0
    for i in range(1, n + 1):
        dist = x[i] - x[i - 1]
        sumcal += v[i] - dist
        if sumcal > maxcal:
            maxcal = sumcal
            pos = x[i]
        l[i] = (maxcal, pos)


f(lst1, x1, v1)
f(lst2, x2, v2)
ans = 0
for i in range(n + 1):
    ans = max(ans, lst1[i][0] + lst2[n - i][0] - min(lst1[i][1], lst2[n - i][1]))
print(ans)
