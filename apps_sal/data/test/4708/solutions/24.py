N = int(input())
K = int(input())
X = int(input())
Y = int(input())
if N <= K:
    account = N * X
else:
    account = K * X + max(N - K, 0) * Y
print(account)
