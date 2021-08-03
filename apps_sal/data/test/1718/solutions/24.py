N, K = map(int, input().split())
*A, = map(int, input().split())
now = 0
ans = 0
while now < N:
    ans += 1
    now += K
    if now >= N:
        break
    now -= 1
print(ans)
