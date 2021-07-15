import sys
input = sys.stdin.readline

n,m = list(map(int,input().split()))
edge = [[] for _ in [0]*n]
for i in range(m):
    u,v = list(map(int,input().split()))
    edge[u-1].append(v-1)
    edge[v-1].append(u-1)

#-1:not used -2:used plus:group max
ma = [-1]*n
for i in range(n):
    if ma[i] != -1:
        continue
    tank = []
    new = [i]
    tmp = i
    while len(new) > 0:
        tank = []
        for e in new:
            for go in edge[e]:
                if ma[go] == -1:
                    ma[go] = -2
                    tmp = max(tmp,go)
                    tank.append(go)
        new = tank
    ma[i] = tmp
#print(ma)
res = 0
p = -1
for i in range(n):
    if ma[i] >= 0:
        if i < p:
            res += 1
        p = max(p,ma[i])
print(res)

