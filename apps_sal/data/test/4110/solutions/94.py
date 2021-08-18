n, k = map(int, input().split())
L = []
for i in range(n):
    a, b = map(int, input().split())
    L.append([(i + 1) * 100, a, b])
ans = 10**10
if k < L[-1][0] * L[-1][1]:
    if k % L[-1][0] != 0:
        ans = (k // L[-1][0] + 1)
    else:
        ans = (k // L[-1][0])

for i in range(1 << n):
    li = []
    score, score_zan, cnt = 0, 0, 0
    for j in range(n):
        if i >> j & 1:
            score += (L[j][0] * L[j][1] + L[j][2])
            cnt += L[j][1]
            score_zan = k - score
        else:
            li.append(L[j])
    if score > 0 and score_zan <= 0:
        ans = min(ans, cnt)
    li.sort(reverse=True)
    if li and score_zan > 0:
        if score_zan < li[0][0] * li[0][1]:
            ans = min(ans, cnt + score_zan // li[0][0])
print(ans)
