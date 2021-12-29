(N, M, X) = map(int, input().split())
CA = [list(map(int, input().split())) for _ in range(N)]
ans = -1
for i in range(1 << N):
    bit = [0] * N
    for j in range(N):
        div = 1 << j
        bit[j] = i // div % 2
    res = [0] * M
    cost = 0
    for n in range(N):
        if bit[n] == 0:
            continue
        cost += CA[n][0]
        for m in range(1, M + 1):
            res[m - 1] += CA[n][m]
    flag = True
    for m in range(M):
        if res[m] < X:
            flag = False
            break
    if flag:
        if ans == -1:
            ans = cost
        else:
            ans = min(ans, cost)
print(ans)
