import sys
from collections import deque


def IN_I(): return int(sys.stdin.readline().rstrip())
def IN_LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def IN_S(): return sys.stdin.readline().rstrip()
def IN_LS(): return list(sys.stdin.readline().rstrip().split())


H, W = IN_LI()
s = [IN_S() for _ in range(H)]

dh = [-1, 0, 1, 0]
dw = [0, -1, 0, 1]

dist = [[-1] * W for j in range(H)]
dist[0][0] = 0

q = deque()
q.append([0, 0])

while q:
    now = q.popleft()
    now_h = now[0]
    now_w = now[1]

    for i in range(4):
        next_h = now_h + dh[i]
        next_w = now_w + dw[i]

        if not (0 <= next_h < H and 0 <= next_w < W):
            continue
        if s[next_h][next_w] == '#':
            continue

        if dist[next_h][next_w] == -1:
            q.append([next_h, next_w])
            dist[next_h][next_w] = dist[now_h][now_w] + 1

if dist[-1][-1] == -1:
    print((-1))
    return

black = sum([i.count('#') for i in s])
ans = (H * W - black) - (dist[-1][-1] + 1)
print(ans)
