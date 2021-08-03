N, K = [int(x) for x in input().split()]
X = [int(x) for x in input().split()]


ans = float("inf")
for i in range(N - K + 1):
    left = X[i]
    right = X[i + K - 1]
    if left * right >= 0:
        ans = min(ans, max(abs(left), right))
    else:
        ans = min(ans, right - left + min(abs(left), right))
print(ans)
