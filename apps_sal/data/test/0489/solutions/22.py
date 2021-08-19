from math import factorial


def c(n, k):
    return factorial(n) // factorial(k) // factorial(n - k)


n = int(input())
a = list(map(int, input().split()))
a.sort()
(f, s, t) = (0, 0, 0)
(i, j, k) = (0, 0, 0)
f = a[:3].count(a[0])
if f == 1:
    s = a[:3].count(a[1])
    if s == 1:
        t = 1
elif f == 2:
    s = 1
p = 1
while p < n and a[p] == a[p - 1]:
    p += 1
i = p
if p < n:
    p += 1
    while p < n and a[p] == a[p - 1]:
        p += 1
    j = p - i
    if p < n:
        p += 1
        while p < n and a[p] == a[p - 1]:
            p += 1
        k = p - j - i
print(c(i, f) * c(j, s) * c(k, t))
