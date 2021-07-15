H, W = map(int, input().split())
N = int(input())
a = list(map(int,input().split()))

g = [[1]*(W+2)]
for i in range(H):
    g.append([1] + [0]*W + [1])
g.append([1]*(W+2))

temp = [[1, 1]]
g[1][1] = 1
c, cnt = 1, 0
while temp:
    p = temp.pop()
    for y, x in [[0, 1], [0, -1], [1, 0]]:
        if g[p[0]+y][p[1]+x] == 0:
            temp.append([p[0]+y, p[1]+x])
            if c == a[cnt]:
                cnt += 1
                c = 1
            else: c += 1
            g[p[0]+y][p[1]+x] = cnt+1
            break
for gg in g[1:-1]:
    print(*gg[1:-1])
