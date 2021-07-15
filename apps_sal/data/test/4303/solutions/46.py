N, K = map(int, input().split())
X = list(map(int, input().split()))

ans = 10 ** 10
nega = sorted(-x for x in X if x < 0)
posi = sorted(x for x in X if 0 < x)
if 0 in X:
    K -= 1

if 0 < K <= len(posi):
    t = posi[K - 1]
    ans = min(ans, t)
if 0 < K <= len(nega):
    t = nega[K - 1]
    ans = min(ans, t)

if 0 < K:
    for np in range(1, len(posi) + 1):
        if 0 <= K - np - 1 < len(nega):
            t = posi[np - 1] * 2 + nega[K - np - 1]
            ans = min(ans, t)
    for nn in range(1, len(nega) + 1):
        if 0 <= K - nn - 1 < len(posi):
            t = nega[nn - 1] * 2 + posi[K - nn - 1]
            ans = min(ans, t)
else:
    ans = 0
print(ans)
