from sys import stdin, stdout
n = int(stdin.readline())
power = [2 ** i for i in range(31)]
d = {}
ans = 0
for value in map(int, stdin.readline().split()):
    for m in power:
        if m >= value and m - value in d:
            ans += d[m - value]
    if value in d:
        d[value] += 1
    else:
        d[value] = 1
stdout.write(str(ans))
