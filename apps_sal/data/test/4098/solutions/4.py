(n, K) = map(int, input().split())
arr = sorted(map(int, input().split()))
freq = {}
for x in arr:
    freq[x] = freq.get(x, 0) + 1
arr = sorted(freq.keys())
freq = [freq[x] for x in arr]
n = len(arr)
dp = [[0 for _ in range(n + 1)] for _ in range(2)]
for k in range(1, K + 1):
    for i in range(n - 1, -1, -1):
        j = i
        curr = 0
        curr_ans = dp[k & 1][i + 1]
        while j < n and abs(arr[i] - arr[j]) <= 5:
            curr += freq[j]
            curr_ans = max(curr_ans, curr + dp[1 - (k & 1)][j + 1])
            j += 1
        dp[k & 1][i] = curr_ans
print(dp[K & 1][0])
