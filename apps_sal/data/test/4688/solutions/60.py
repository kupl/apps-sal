(N, K) = map(int, input().split())
pr = K
for _ in range(1, N):
    pr *= K - 1
print(pr)
