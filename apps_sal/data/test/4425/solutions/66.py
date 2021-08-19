(N, K) = map(int, input().split())
ans = 0
for i in range(1, N + 1):
    j = 0
    while True:
        if K <= i * 2 ** j:
            ans += 1 / N * (1 / 2) ** j
            break
        j += 1
print(ans)
