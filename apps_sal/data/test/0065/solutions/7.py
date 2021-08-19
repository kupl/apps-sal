from sys import stdin, stdout
INF = float('inf')
n = int(stdin.readline())
values = list(map(int, stdin.readline().split()))
ans = INF
previous = -INF
mn = min(values)
for i in range(n):
    if values[i] == mn:
        ans = min(ans, i - previous)
        previous = i
stdout.write(str(ans))
