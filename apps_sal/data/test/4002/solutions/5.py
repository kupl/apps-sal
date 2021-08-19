(n, m, k) = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(n)]
dp1 = []
for i in range(n):
    B = A[i]
    temp = [[-1] * k for _ in range(m // 2 + 1)]
    temp[0][0] = 0
    for b in B:
        for l in reversed(list(range(m // 2))):
            for j in range(k):
                if temp[l][j] != -1:
                    temp[l + 1][(b + j) % k] = max(temp[l + 1][(b + j) % k], temp[l][j] + b)
    temp2 = [-1] * k
    for j in range(k):
        for l in range(m // 2 + 1):
            temp2[j] = max(temp2[j], temp[l][j])
    dp1.append(temp2)
dp2 = [[-1] * k for i in range(n + 1)]
dp2[0][0] = 0
for i in range(n):
    for j in range(k):
        dp2[i + 1][j] = dp2[i][j]
    for j in range(k):
        if dp1[i][j] == -1:
            continue
        for l in range(k):
            if dp2[i][l] == -1:
                continue
            dp2[i + 1][(j + l) % k] = max(dp2[i + 1][(j + l) % k], dp2[i][l] + dp1[i][j])
ans = dp2[n][0]
print(max(ans, 0))
