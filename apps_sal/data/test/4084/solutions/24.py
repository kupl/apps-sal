(n, a, b) = map(int, input().split(' '))
(q, r) = divmod(n, a + b)
s = q * a
if r > a:
    s += a
else:
    s += r
print(s)
