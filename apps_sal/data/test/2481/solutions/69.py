(H, W) = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(10)]
cost = [99999] * 10
cost[1] = 0


def f(n):
    for i in range(10):
        flag = False
        cc = C[i][n] + cost[n]
        if cc < cost[i]:
            flag = True
            cost[i] = cc
            f(i)


f(1)
ans = 0
for _ in range(H):
    for n in map(int, input().split()):
        if n < 0:
            continue
        ans += cost[n]
print(ans)
