
N, K = list(map(int, input().split()))
answer = 0
for i in range(1, N + 1):
    cnt = 0
    while i < K:
        i *= 2
        cnt += 1
    answer += (1 / 2)**cnt

print((answer / N))
