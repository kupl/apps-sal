from collections import deque
h, w, k = list(map(int, input().split()))
x1, y1, x2, y2 = list(map(int, input().split()))
x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1

m = [[-1] * w for _ in range(h)]
for hh in range(h):
    c = input()
    for ww, cc in enumerate(c):
        if cc == '.':
            m[hh][ww] = h * w

q = deque()

q.append((0, x1, y1))
while q:
    s, x, y = q.popleft()
    s1 = s + 1

    for i in range(1, k + 1):
        xx, yy = x + i, y
        if xx >= h or m[xx][yy] <= s:
            break
        if m[xx][yy] == s1:
            continue
        if xx == x2 and yy == y2:
            print(s1)
            return
        m[xx][yy] = s1
        q.append((s1, xx, yy))

    for i in range(1, k + 1):
        xx, yy = x - i, y
        if xx < 0 or m[xx][yy] <= s:
            break
        if m[xx][yy] == s1:
            continue
        if xx == x2 and yy == y2:
            print(s1)
            return
        m[xx][yy] = s1
        q.append((s1, xx, yy))

    for i in range(1, k + 1):
        xx, yy = x, y + i
        if yy >= w or m[xx][yy] <= s:
            break
        if m[xx][yy] == s1:
            continue
        if xx == x2 and yy == y2:
            print(s1)
            return
        m[xx][yy] = s1
        q.append((s1, xx, yy))

    for i in range(1, k + 1):
        xx, yy = x, y - i
        if yy < 0 or m[xx][yy] <= s:
            break
        if m[xx][yy] == s1:
            continue
        if xx == x2 and yy == y2:
            print(s1)
            return
        m[xx][yy] = s1
        q.append((s1, xx, yy))

print((-1))
