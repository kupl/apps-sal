(n, k) = map(int, input().split())
ans = 0
for i in range(1, n + 1):
    cnt = 0
    while i < k:
        i *= 2
        cnt += 1
    ans += 1 / n / 2 ** cnt
print(ans)
