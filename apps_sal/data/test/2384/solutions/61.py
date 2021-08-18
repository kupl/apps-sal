from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
dp = defaultdict(lambda: -pow(10, 18))
dp[(1, 1)] = a[0]
for i in range(2, n + 1):
    for j in range(i // 2 - 1, (i + 1) // 2 + 1):
        if j == 1:
            dp[(i, j)] = max(dp[(i - 1, 1)], a[i - 1])
        elif j == 0:
            dp[(i, j)] = 0
        else:
            dp[(i, j)] = max(dp[(i - 2, j - 1)] + a[i - 1], dp[(i - 1, j)])
print(dp[(n, n // 2)])
