import sys
sys.setrecursionlimit(100000)

def find(x,y,tag):
    if mplake[x][y] == tag or mp[x][y] == "*":
        return
    mplake[x][y] = tag
    lakes[tag] += 1
    for i in [(1,0),(-1,0),(0,1),(0,-1)]:
        if 0 <= x+i[0] and x+i[0] < n and 0 <= y + i[1] and y+i[1] < m:
            find(x+i[0],y+i[1],tag)

def fill(x,y,tag):
    nonlocal cnt
    if mplake[x][y] == tag:
        mplake[x][y] = -1
        mp[x][y] = "*"
        cnt += 1
        for i in [(1,0),(-1,0),(0,1),(0,-1)]:
            if 0 <= x+i[0] and x+i[0] < n and 0 <= y + i[1] and y+i[1] < m:
                fill(x+i[0],y+i[1],tag)

n, m, k = [int(i) for i in input().split()]
mp = []
mplake = []
for i in range(n):
    mp.append(list(input()))
    mplake.append([-1 for i in range(m)])

start = [(0,0)]
lakes = [0]
cnt = 0

for i in range(n):
    find(i,0,0)
    find(i,m-1,0)
for i in range(m):
    find(0,i,0)
    find(n-1,i,0)

for i in range(1,n-1):
    for j in range(1,m-1):
        if mp[i][j] == "." and mplake[i][j] == -1:
            start.append((i,j))
            lakes.append(0)
            find(i,j,len(lakes)-1)

r = sorted([(lakes[i],start[i]) for i in range(1,len(lakes))])

for i in range(len(r)-k):
    fill(r[i][1][0],r[i][1][1],mplake[r[i][1][0]][r[i][1][1]])

print(cnt)
for i in range(n):
    print("".join(mp[i]))

