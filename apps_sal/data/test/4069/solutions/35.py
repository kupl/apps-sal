(X, K, D) = list(map(int, input().split()))
N = X // D
if K < abs(N):
    ans = abs(abs(X) - K * D)
elif (K - abs(N)) % 2 == 0:
    ans = abs(X - N * D)
else:
    ans = abs(X - (N + 1) * D)
print(ans)
