def f(k):
    cur = sum(sorted([a[i] + (i + 1) * k for i in range(n)])[:k])
    return cur, cur <= S


def read(): return map(int, input().split())


n, S = read()
a = list(read())
l, r = 0, n + 1
while r - l > 1:
    m = (l + r) >> 1
    if f(m)[1]:
        l = m
    else:
        r = m
print(l, f(l)[0])
