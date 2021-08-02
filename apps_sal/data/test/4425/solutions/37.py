N, K = map(int, input().split())
ans = 0
for n in range(1, N + 1):
    score = n
    coin = 0
    while(score < K):
        coin += 1
        score *= 2
    ans += 1 / (N * 2**coin)

print(ans)
