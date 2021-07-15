s = n = int(input()) + 1
t, r = [], list(range(n))[::-1]
k = 2 ** 20

while s:
    while k >= 2 * s: k //= 2
    t = r[n - s: n + s - k] + t
    s = k - s

print(n*(n-1))
print(*t)
