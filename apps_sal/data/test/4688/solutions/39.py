(N, K) = map(int, input().split())
cnt = K
for i in range(N - 1):
    cnt *= K - 1
print(cnt)
