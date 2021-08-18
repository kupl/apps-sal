
h, w, K = map(int, input().split())
maze = []
cnt = 0
ans = 0
for i in range(h):
    s = input()
    cnt += s.count("
    li=[c for c in s]
    maze.append(li)

for i in range(2**h):
    c=0
    height=[]
    for j in range(h):
        if (i >> j) & 1:
            height.append(j)
    for y in height:
        for x in range(w):
            if maze[y][x] == "
                c += 1

    for k in range(2**w):
        d=0
        width=[]
        for l in range(w):
            if (k >> l) & 1:
                width.append(l)
        for y in range(h):
            for x in width:
                if maze[y][x] == "
                    d += 1
        total=c + d
        for y in height:
            for x in width:
                if maze[y][x] == "
                    total -= 1
        if cnt - total == K:
            ans += 1
print(ans)
