from collections import deque

h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

sl = []
flag = False
for i in range(h):
    for j in range(w):
        if s[i][j] == '.':
            sl.append([i, j])

q = deque()
dire = [(0, 1), (0, -1), (1, 0), (-1, 0)]
ans = 0
for sh, sw in sl:
    c = [[0]*w for _ in range(h)]
    q.append((sh, sw, 0))
    while q:
        ph, pw, k = q.pop()
        if c[ph][pw] == 0:
            ans = max(ans, k)
            c[ph][pw] = 1
            for dh, dw in dire:
                hdh, wdw = ph+dh, pw+dw
                if 0 <= hdh < h and 0 <= wdw < w and c[hdh][wdw] == 0:
                    if s[hdh][wdw] == '.':
                        q.appendleft((hdh, wdw, k+1))

print(ans)
