# 解説放送の方針
# ダメージが消える右端をキューで管理
# 右端を超えた分は、累積ダメージから引いていく

from collections import deque

N, D, A = map(int, input().split())
XH = [tuple(map(int, input().split())) for _ in range(N)]

XH = sorted(XH)
que = deque()
cum = 0
ans = 0
for i in range(N):
    x, h = XH[i]
    if i == 0:
        r, n = x + 2 * D, (h + A - 1) // A
        d = n * A
        cum += d
        que.append((r, d))
        ans += n
        continue
    while que and que[0][0] < x:
        r, d = que.popleft()
        cum -= d
    h -= cum
    if h < 0:
        continue
    r, n = x + 2 * D, (h + A - 1) // A
    d = n * A
    cum += d
    que.append((r, d))
    ans += n

print(ans)
