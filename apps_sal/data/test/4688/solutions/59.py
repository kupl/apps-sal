N, K = list(map(int, input().split()))
ans = 1

ans = K * (K - 1) ** (N - 1)

print(ans)
