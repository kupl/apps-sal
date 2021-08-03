from sys import stdin, stdout

INF = float('inf')

n, a, b = map(int, stdin.readline().split())

l, r = 1, 200
while r - l > 1:
    m = (l + r) >> 1

    if (b // m and a // m and a // m + b // m >= n):
        l = m
    else:
        r = m

stdout.write(str(l))
