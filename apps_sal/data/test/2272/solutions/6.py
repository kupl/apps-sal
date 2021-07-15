n = int(input())
xy = []
adjlist = []

def dfs(visit,cur,dest):
    visit[cur] = True
    if cur==dest: return True
    else:
        found = False
        for v in adjlist[cur] :
            if not visit[v] :
                found = found or dfs(visit,v,dest)
        return found

for tc in range(0,n):
    q, a, b = [int(x)-1 for x in input().split()]
    if q == 0:
        adjlist.append([])
        for i in range(0,len(xy)):
            x,y = xy[i]
            if (a<x<b or a<y<b):
                adjlist[i].append(len(xy))
            if (x<a<y or x<b<y):
                adjlist[len(xy)].append(i)
        xy.append((a,b))
    elif q == 1:
        visit = [False for x in range(0,len(xy))]
        if dfs(visit,a,b):
            print("YES")
        else:
            print("NO")

