import sys


def minp():
    return sys.stdin.readline().strip()


n, m = map(int, minp().split())
a = minp()
b = minp()
c = 0
if n >= m:
    i = n - m
    j = 0
else:
    for j in range(m - n):
        if b[j] == '1':
            c += 1
    i = 0
    j = m - n
r = 0
while i < n:
    r = (r * 2) % 998244353
    if b[j] == '1':
        c += 1
    if a[i] == '1':
        r += c
    i += 1
    j += 1
print(r % 998244353)
