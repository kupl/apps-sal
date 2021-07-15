n, k = map(int, input().split())

cnt = 0
for ac in range(1 - n, n):
    bd = k - ac
    if 1 - n <= bd <= n - 1:
        cnt += (n - abs(ac)) * (n - abs(bd))

print(cnt)
