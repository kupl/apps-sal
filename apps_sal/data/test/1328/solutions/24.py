n, ma, mb = map(int, input().split())
abc = []
for _ in range(n):
    a, b, c = map(int, input().split())
    abc.append((a, b, c))
dp = {(0, 0): 0}
for a, b, c in abc:
    newdp = dp.copy()
    for (ka, kb), p in dp.items():
        k = (a + ka, b + kb)
        if k in newdp:
            newdp[k] = min(newdp[k], p + c)
        else:
            newdp[k] = p + c
    dp = newdp
INF = 10**10
ans = INF
for (a, b), c in dp.items():
    if ma * b != mb * a or a == b == 0:
        continue
    ans = min(ans, c)
if ans == INF:
    print(-1)
else:
    print(ans)
