(n, x) = map(int, input().split())
t = list(map(int, input().split()))
m = min(t[:x])
if m == 0:
    i = x - 1
    while t[i]:
        i -= 1
    t[i + 1:x] = [j - 1 for j in t[i + 1:x]]
    t[i] = x - i - 1
else:
    t[:x] = [i - 1 for i in t[:x]]
    m = min(t)
    if m:
        t = [i - m for i in t]
    i = n - 1
    while t[i]:
        i -= 1
    t[i + 1:] = [j - 1 for j in t[i + 1:]]
    t[i] = x + m * n + n - i - 1
print(' '.join(map(str, t)))
