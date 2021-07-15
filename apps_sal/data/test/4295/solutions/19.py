N,K = map(int,input().split())
n = N - K * (N//K)
n = min(n, abs(n-K))
print(n)
