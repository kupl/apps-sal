N, K = map(int, input().split())

ans = 0
for i in range(1, N + 1):
    cnt = 0
    num = i
    while num < K:
        num *= 2
        cnt += 1
    ans += 1 / N * (1 / 2)**cnt
print(ans)
