from sys import stdin, stdout
n = int(stdin.readline())
values = sorted(list(map(int, stdin.readline().split())))
ans = min(values)
for i in range(n):
    if values[i] >= 0:
        x = values[i] ** 0.5
        if int(x) != x:
            ans = max(ans, values[i])
    else:
        ans = values[i]
stdout.write(str(ans))
