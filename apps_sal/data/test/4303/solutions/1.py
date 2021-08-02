N, K = list(map(int, input().split()))
X = list(map(int, input().split()))
a = []
for i in range(N - K + 1):
    l = X[i]
    r = X[i + K - 1]
    a.append(min(abs(l) + abs(r - l), abs(r) + abs(r - l)))
print((min(a)))
