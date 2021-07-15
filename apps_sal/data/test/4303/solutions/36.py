N, K = list(map(int, input().split()))
X = [int(x) for x in input().split()]
ans = 10**10

for i in range(N-K+1):
    tmp = X[i+K-1] - X[i] + min(abs(X[i+K-1]), abs(X[i]))
    if tmp < ans:
        ans = tmp
print(ans)

