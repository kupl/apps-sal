N, K = map(int, input().split())

ans = min(N - K * (N // K), K - (N - K * (N // K)))

print(ans)
