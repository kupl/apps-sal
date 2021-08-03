a, b = '0' + input(), '0' + input()
m, n = len(a), len(b)
c, s = [0] * (n + 1), 0
if m <= n:
    for i in range(1, n):
        c[i] = int(b[i]) + c[i - 1]
    for i in range(1, m):
        if a[i] == '0':
            s += c[i + n - m] - c[i - 1]
        else:
            s += n - m + 1 - (c[i + n - m] - c[i - 1])
print(s)
