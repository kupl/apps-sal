n = int(input())
f = lambda x: x * x + sum(map(int, str(abs(x)))) * x


def b(l, r):
    while l < r - 1:
        m = (l + r) // 2
        if f(m) < n: l = m
        else: r = m
    return r


r = b(0, 10**18)
for i in range(max(1, r - 1000), r + 1000):
    if f(i) == n: r = i; break
else: r = -1
print(r)
