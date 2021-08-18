N, K = map(int, input().split())

ans = 0

for i in range(1, N + 1):
    t = 0
    while True:
        if i * (2**t) >= K:
            break
        t += 1
    ans += (1 / N) * ((1 / 2)**t)

print(ans)
