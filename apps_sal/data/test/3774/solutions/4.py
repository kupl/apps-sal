(n, m) = map(int, input().split())
a = n * m
if n > m:
    (n, m) = (m, n)
if n == 1:
    a -= min(m % 6, 6 - m % 6)
elif n == 2:
    a -= 2 * (abs(5 - m) == 2) + 4 * (m == 2)
else:
    a -= n & 1 * m & 1
print(a)
