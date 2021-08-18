n, K = map(int, input().split())

p = 1 / n

ans = 0
for result in range(1, n + 1):
    k = K
    k /= result
    cnt = 0
    while k > 1:
        k /= 2
        cnt += 1
    ans += p * (0.5)**cnt
print(ans)
