(n, m, q) = list(map(int, input().split()))
tmp = [[0] * 510 for _ in range(510)]
for _ in range(m):
    (l, r) = list(map(int, input().split()))
    tmp[l][r] += 1
for i in range(1, 501):
    for j in range(1, 501):
        tmp[i][j] += tmp[i - 1][j]
        tmp[i][j] += tmp[i][j - 1]
        tmp[i][j] -= tmp[i - 1][j - 1]
for _ in range(q):
    ans = 0
    (ll, rr) = list(map(int, input().split()))
    print(tmp[rr][rr] - tmp[rr][ll - 1] - tmp[ll - 1][rr] + tmp[ll - 1][ll - 1])
