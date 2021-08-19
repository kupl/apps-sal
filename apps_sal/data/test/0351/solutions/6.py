from sys import stdin, stdout
EPS = 10 ** (-20)
INF = float('inf')
size = 10 ** 6
(n, k) = map(int, stdin.readline().split())
values = sorted(list(map(int, stdin.readline().split())))
i = 0
ans = 0
while i < n:
    if 2 * k >= values[i]:
        k = max(k, values[i])
        i += 1
    else:
        k *= 2
        ans += 1
stdout.write(str(ans))
