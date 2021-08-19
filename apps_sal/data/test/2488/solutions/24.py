from math import ceil
from collections import deque
N, D, A = list(map(int, input().split()))
XH = [list(map(int, input().split())) for _ in range(N)]
XH.sort(key=lambda x: x[0])
ans = 0

XN = [[x, ceil(h / A)] for x, h in XH]
# 左端のモンスターに攻撃が必要な回数はそこから2*Dだけ右にあるモンスターにまで波及できる
cnum = 0
que = deque()
ans = 0
for x, n in XN:
    while que and x > que[0][0]:
        _, num = que.popleft()
        cnum -= num
    need = max(0, n - cnum)
    ans += need
    cnum += need

    if need:
        que.append([x + 2 * D, need])
print(ans)
