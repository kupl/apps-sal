N = int(input())
K = int(input())
X = int(input())
Y = int(input())
ans = 0

if N > K:
    for i in range(0, K):
        ans += X
    for i in range(K, N):
        ans += Y
elif N <= K:
    for i in range(0, N):
        ans += X

print(ans)
