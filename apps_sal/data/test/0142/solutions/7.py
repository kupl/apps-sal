from sys import stdin, stdout


sze = 100
INF = float('inf')

n, l = map(int, stdin.readline().split())
c = list(map(int, stdin.readline().split()))
may = [1 for i in range(sze)]

for i in range(n - 1, -1, -1):
    for j in range(i):
        if c[i] > c[j] * 2 ** (i - j):
            may[i] = 0


ans = INF

cnt = 0
value = 0

for i in range(n - 1, -1, -1):
    if not may[i]:
        continue

    v = l - value

    if not v % (2 ** i):
        ans = min(ans, cnt + v * c[i] // (2 ** i))
    else:
        ans = min(ans, cnt + (v // (2 ** i) + 1) * c[i])

    cnt += v // (2 ** i) * c[i]
    value += (v // (2 ** i)) * (2 ** i)

stdout.write(str(ans))
