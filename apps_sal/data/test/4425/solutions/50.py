(n, k) = map(int, input().split())
ans = 0
for tmp in range(1, n + 1):
    cnt = 0
    while tmp < k:
        tmp *= 2
        cnt += 1
    ss = n * 2 ** cnt
    ans += 1 / ss
print(ans)
