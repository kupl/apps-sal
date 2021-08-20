n = int(input())
N = 2 * n
ans = [None] * N
a = [list(map(int, input().split())) for i in range(N - 1)]
used = [False] * N
inf = 10 ** 9
for i in range(n):
    Max = -inf
    for i in range(N - 1):
        if not used[i + 1]:
            for j in range(i + 1):
                if not used[j] and a[i][j] > Max:
                    Max = a[i][j]
                    (x, y) = (i + 1, j)
    used[x] = True
    used[y] = True
    ans[x] = y + 1
    ans[y] = x + 1
print(' '.join(map(str, ans)))
