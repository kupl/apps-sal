(N, T) = map(int, input().split())
X = list(map(int, input().split()))
S = 0
for i in range(1, N):
    if X[i] - X[i - 1] >= T:
        S += T
    else:
        S += X[i] - X[i - 1]
print(S + T)
