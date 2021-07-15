n = int(input())
a = [int(i) for i in input().split()]

#a_set = set(a)
prefix = dict()
suffix = dict()
for i in range(n):
    if a[i] not in prefix:
        prefix[a[i]] = i
    suffix[a[i]] = i
dp = [ 0 for i in range(n+1)]
for i in range(n):
    dp[i] = dp[i-1]
    if suffix[a[i]] != i:
        continue
    cur = 0
    min_ind = prefix[a[i]]
    for j in range(i, -1, -1):
        if suffix[a[j]] <= i:
            if suffix[a[j]] == j:
                cur = cur ^ a[j]
            min_ind = min(min_ind, prefix[a[j]])
            if j == min_ind:
                dp[i] = max(dp[i], dp[j-1] + cur)
        else:
            break
print(dp[n-1])
