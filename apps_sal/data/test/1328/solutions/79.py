N, Ma, Mb = list(map(int, input().split()))

INF = 10 ** 8

lst = [[INF] * 401 for i in range(401)]
lst[0][0] = 0

for _ in range(N):
    a, b, c = list(map(int, input().split()))
    for i in range(400, a - 1, -1):
        for j in range(400, b - 1, -1):
            if lst[i - a][j - b] == INF:
                pass
            else:
                lst[i][j] = min(lst[i][j], lst[i - a][j - b] + c)

ans = INF
n = 400 // max(Ma, Mb)
for i in range(1, n + 1):
    ans = min(ans, lst[Ma * i][Mb * i])

if ans == INF:
    print((-1))
else:
    print(ans)

# for i in range(7):
#     print (lst[i][:7])
