n = int(input())
a = list(map(int, input().split()))
def md(x, d):
    res = 0
    dd = 1
    while x % (dd * d) == 0:
        dd *= d
        res += 1
    return res
 
def cmp(a, b):
    d3a = md(a, 3)
    d2a = md(a, 2)
    d3b = md(b, 3)
    d2b = md(b, 2)
    if d3a == d3b:
        return d2a < d2b
    return d3a > d3b
for i in range(n):
    for j in range(i, n):
        if cmp(a[j], a[i]):
            a[i], a[j] = a[j], a[i]
print(" ".join(map(str, a)))
