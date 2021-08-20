from math import log
(n, k) = map(int, input().split())
a = list(map(int, input().split()))
(i, s) = (0, {})
if k == -1:
    s = {1: 0, -1: 0}
elif k == 1:
    s = {1: 0}
else:
    while max(-k ** i, k ** i) <= 10 ** 9 * n:
        s[k ** i] = 0
        i += 1
(d, p) = ({0: 1}, 0)
for i in a:
    p += i
    if p in d:
        d[p] += 1
    else:
        d[p] = 1
    for j in s:
        if p - j in d:
            s[j] += d[p - j]
r = 0
for i in s:
    r += s[i]
print(r)
