from sys import stdin, stdout

n = int(stdin.readline())
values = sorted(list(map(int, stdin.readline().split())))
ans = float('inf')

for i in range(2 * n):
    for j in range(i + 1, 2 * n):
        res = []

        for z in range(2 * n):
            if z == i or z == j:
                continue

            res.append(values[z])

        cnt = 0
        for q in range(0, len(res), 2):
            cnt += res[q + 1] - res[q]

        ans = min(ans, cnt)

stdout.write(str(ans))
