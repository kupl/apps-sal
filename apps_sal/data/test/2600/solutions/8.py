T = int(input())
for __ in range(T):
    n, m = map(int, input().split())
    A = []
    for __ in range(n):
        A.append(list(map(int, input().split())))
    D = [[0, 0] for __ in range(n + m - 1)]
    for i in range(n):
        for j in range(m):
            D[i + j][A[i][j]] += 1
    ans = 0
    for k1 in range((n + m - 1) // 2):
        k2 = (n + m - 2) - k1
        x = min(D[k1][0] + D[k2][0], D[k1][1] + D[k2][1])
        ans += x
        # print(k1, k2, x)
    # print(D)
    print(ans)
