n = int(input())
a = list(map(int, input().split()))
t = [0] * 2 * n
s = 0
for i in range(n):
    d = a[i] - i - 1
    s += abs(d)
    if d > 0:
        t[d] += 1
p = sum(t)
r = (s, 0)
for i in range(1, n):
    d = a[n - i] - 1
    s += d - p << 1
    t[d + i] += d > 0
    p += (d > 0) - t[i]
    if s < r[0]:
        r = (s, i)
print(*r)
