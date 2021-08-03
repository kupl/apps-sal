def R(): return map(int, input().split())


prime, cnt = [1] * 10001, [0] * 10001
pms = []
for i in range(2, 10001):
    if prime[i]:
        for j in range(i + i, 10001, i):
            prime[j] = 0
        pms.append(i)
n = int(input())
for x in R():
    mx = 0
    coms = []
    for p in pms:
        if x < p:
            break
        if x % p == 0:
            mx = max(mx, cnt[p] + 1)
            coms.append(p)
    for x in coms:
        cnt[x] = mx
print(max(cnt + [1]))
