from collections import deque
import sys
input = sys.stdin.readline
N, D, A = list(map(int, input().split()))
xh = [list(map(int, input().split())) for _ in range(N)]
xh = sorted(xh)
total = 0  # 今与えているダメージの総和
D = 2 * D
ans = 0
q = deque()
for i in range(N):
    x, h = xh[i]
    # 今いる場所が前回までの爆撃の範囲外になるならその分totalから引く
    while len(q) >= 1 and q[0][0] < x:
        total -= q.popleft()[1]
    h -= total

    if h > 0:
        num = (h - 1) // A + 1
        ans += num
        damage = num * A
        total += damage
        q += ([[x + D, damage]])

print(ans)
