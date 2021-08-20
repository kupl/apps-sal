(N, A, B) = map(int, input().split())
vlist = list(map(int, input().split()))
vlist.sort(reverse=True)
dp = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        dp[i][j] = dp[i - 1][j]
        dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + vlist[i - 1])
max_value_avg = 0
for j in range(A, B + 1):
    value_avg = dp[-1][j] / j
    max_value_avg = max(max_value_avg, value_avg)
max_avg_size = []
for j in range(A, B + 1):
    value_avg = dp[-1][j] / j
    if value_avg == max_value_avg:
        max_avg_size.append(j)


def comb(n, r):
    r = min(r, n - r)
    nPr = 1
    fact_r = 1
    for i in range(r):
        nPr *= n - i
        fact_r *= r - i
    return nPr // fact_r


answer = 0
for m in max_avg_size:
    border = vlist[m - 1]
    n1 = n2 = n3 = 0
    for v in vlist:
        if v > border:
            n1 += 1
        elif v == border:
            n2 += 1
        else:
            n3 += 1
    answer += comb(n2, m - n1)
print(max_value_avg)
print(answer)
