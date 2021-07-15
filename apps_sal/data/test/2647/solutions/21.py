from collections import deque
h, w = map(int, input().split())
s = [list(input()) for i in range(h)]
ans = sum([i.count("#") for i in s])
s = [["#"]*(w+2)] + [["#"]+i+["#"] for i in s] + [["#"]*(w+2)]
d = deque([[1, 1, 1]])
while len(d) > 0:
    x, y, cnt = d.popleft()
    if x == h and y == w:
        print(h*w-cnt-ans)
        return
    s[x][y] = "#"
    if s[x-1][y] == ".":
        d.append([x-1, y, cnt+1])
        s[x-1][y] = "#"
    if s[x+1][y] == ".":
        d.append([x+1, y, cnt+1])
        s[x+1][y] = "#"
    if s[x][y-1] == ".":
        d.append([x, y-1, cnt+1])
        s[x][y-1] = "#"
    if s[x][y+1] == ".":
        d.append([x, y+1, cnt+1])
        s[x][y+1] = "#"
print(-1)
