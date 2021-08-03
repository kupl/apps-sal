X, K, D = map(int, input().split())

cur = abs(X)
cnt = min(cur // D, K)
cur -= cnt * D
K = K - cnt

if K > 0:
    if K % 2 == 1:
        cur = cur - D

print(abs(cur))
