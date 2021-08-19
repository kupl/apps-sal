dicti = {}
INF = -float('inf')


def dp(ind, k):
    if k == 0:
        return 0
    elif ind > diff:
        return INF
    elif (ind, k) in dicti:
        return dicti[ind, k]
    a = max(dp(ind + 1, k), dp(ind + m, k - 1) + sumi[ind])
    dicti[ind, k] = a
    return a


(n, m, k) = map(int, input().strip().split())
diff = n - m
arr = list(map(int, input().strip().split()))
if m == 1:
    arr.sort()
    print(sum(arr[n - k:n]))
else:
    sumi = [0 for i in range(m - 1)]
    sums = sum(arr[:m])
    sumi.append(sums)
    end = m
    for i in range(n - m):
        sums -= arr[i]
        sums += arr[end]
        end += 1
        sumi.append(sums)
    dp = [[0 for i in range(n)] for i in range(k)]
    for i in range(n):
        dp[0][i] = max(sumi[i], dp[0][i - 1])
    for i in range(1, k):
        for j in range(m, n):
            dp[i][j] = max(dp[i][j - 1], sumi[j] + dp[i - 1][j - m])
    print(dp[k - 1][n - 1])
