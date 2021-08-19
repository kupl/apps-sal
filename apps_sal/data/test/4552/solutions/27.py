N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]

# bit全探索
inf = float("inf")
ans = -inf
for i in range(1, 2**10):
    op = []
    for j in range(10):
        if (i >> j) & 1:
            op.append(1)
        else:
            op.append(0)

    res = 0
    for k in range(N):
        temp = 0
        for l in range(10):
            if op[l] == 1 and F[k][l] == 1:
                temp += 1
        res += P[k][temp]
    ans = max(ans, res)

print(ans)
