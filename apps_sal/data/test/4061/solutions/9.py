from sys import stdin, stdout

input = stdin.readline

s, t = list(map(str, stdin.read().split()))

n, m = len(s), len(t)
a = [0] * m
b = [0] * m

pos = 0
for i in range(n):
    if s[i] == t[pos]:
        a[pos] = i
        pos += 1
        if pos == m:
            break

pos = m - 1
for i in range(n - 1, -1, -1):
    if s[i] == t[pos]:
        b[pos] = i
        pos -= 1
        if pos == -1:
            break

res = max(b[0], n - (a[-1] + 1))
for i in range(m - 1):
    res = max(res, (b[i + 1] - 1) - (a[i] + 1) + 1)

print(res)
