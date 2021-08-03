X, K, D = map(int, input().split())
ans = float('inf')
X = abs(X)
before_0_cnt = X // D
if before_0_cnt >= K:
    print(X - K * D)
    return
if (before_0_cnt % 2) ^ (K % 2) == 0:
    print(X - before_0_cnt * D)
else:  # odd
    print(abs(X - before_0_cnt * D - D))
