(n, k) = list(map(int, input().split()))
ans = 0
for i in range(1, n + 1):
    cnt = 0
    while True:
        if 2 ** cnt >= k / i:
            break
        cnt += 1
    ans += 1 / n * (1 / 2) ** cnt
print(ans)
