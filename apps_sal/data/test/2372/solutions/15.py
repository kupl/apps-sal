from collections import deque


def solve(h, w, ch, cw, dh, dw, s):
    W, H = w + 5, h + 5

    def pos(r, c):
        return (r + 2) * W + c + 2
    G = [0] * (W * H)
    label = 0
    for r in range(h):
        for c in range(w):
            if (s[r][c] == '.') and (G[pos(r, c)] == 0):
                label += 1
                que = deque([(r, c)])
                G[pos(r, c)] = label
                while que:
                    cr, cc = que.popleft()
                    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        nr, nc = cr + dr, cc + dc
                        if (0 <= nr < h) and (0 <= nc < w) and (s[nr][nc] == ".") and (G[pos(nr, nc)] == 0):
                            G[pos(nr, nc)] = label
                            que.append((nr, nc))

    start = pos(ch - 1, cw - 1)
    goal = pos(dh - 1, dw - 1)

    neighbors = [(dr * W + dc) for dc in range(-2, 3) for dr in range(-2, 3) if abs(dr) + abs(dc) > 0]
    used = [True] * (W * H)
    for r in range(h):
        for c in range(w):
            used[pos(r, c)] = (s[r][c] == "
    que=deque([(start, 0)])
    label_dist_mapping=[-1] * (label + 1)
    used[start]=True
    label_dist_mapping[G[start]]=0
    while que:
        cpos, n=que.popleft()
        if cpos == goal:
            return n
        for d in neighbors:
            npos=cpos + d
            if not used[npos]:
                used[npos]=True
                m=label_dist_mapping[G[npos]]
                if (G[npos] == G[cpos]) or (n == m):
                    que.appendleft((npos, n))
                else:
                    label_dist_mapping[G[npos]]=n + 1
                    que.append((npos, n + 1))
    return -1


h, w=list(map(int, input().split()))
ch, cw=list(map(int, input().split()))
dh, dw=list(map(int, input().split()))
s=[input() for i in range(h)]
print((solve(h, w, ch, cw, dh, dw, s)))
