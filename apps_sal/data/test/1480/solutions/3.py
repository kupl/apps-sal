n, k = list(map(int, input().split()))
*a, = list(map(int, input().split()))
ans = []
peo = list(range(1, n + 1))

cur = 0
for i in range(k):
    dind = (cur + a[i]) % len(peo)
    cur = dind
    ans.append(peo.pop(dind))
    cur %= len(peo)
    dind %= len(peo)
print(*ans)
