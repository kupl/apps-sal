N, K = list(map(int, input().split()))

t = N % K
print((min(abs(t - K), t)))
