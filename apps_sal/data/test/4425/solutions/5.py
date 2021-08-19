(N, K) = list(map(int, input().split()))
ans = 0
for i in range(N):
    temp = K / (i + 1)
    for j in range(100):
        if 2 ** j >= temp:
            break
    ans += 1 / N * (1 / 2) ** j
print(ans)
