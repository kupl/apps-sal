(N, K) = list(map(int, input().split()))
X = sorted(list(map(int, input().split())))
cnt = []
for i in range(N - K + 1):
    left = X[i]
    right = X[i + K - 1]
    cnt.append(min(abs(right) + abs(left - right), abs(left) + abs(right - left)))
print(min(cnt))
