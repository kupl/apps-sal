from collections import Counter, defaultdict


def R():
    return map(int, input().split())


n = int(input())
arr = list(R())
cnts = Counter(arr)
dp = [0] * (n + 1)
for i in range(n):
    acc = defaultdict(int)
    (cnt, xor) = (0, 0)
    dp[i] = dp[i - 1]
    for j in range(i, -1, -1):
        acc[arr[j]] += 1
        if acc[arr[j]] == cnts[arr[j]]:
            cnt += 1
            xor = xor ^ arr[j]
        if len(acc) == cnt:
            dp[i] = max(dp[i], dp[j - 1] + xor)
print(dp[n - 1])
