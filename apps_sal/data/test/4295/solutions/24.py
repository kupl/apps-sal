N, K = map(int, input().split())
N = N - K * (N // K)
N = min(N, abs(N - K))
print(N)
