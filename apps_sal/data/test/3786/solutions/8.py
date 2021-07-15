def bfs(d,n):
    queue = [[1,0]]
    res = 0
    mark = {i:False for i in range(1,n+1)}
    mark[1]=True
    res = [0 for i in range(n)]
    while queue:
        q = queue.pop(0)
        x,level = q[0],q[1]
        lev = level+1
        res[level]=(res[level]+1)%2
        for i,y in enumerate(d[x]):
            if mark[y]==False:
                mark[y]=True
                queue.append([y,lev])
    print(sum(res))
n = int(input())
lst = list(map(int,input().split()))
d = {1:[]}
for i,x in enumerate(lst):
    d[x].append(i+2)
    d[i+2]=[]
bfs(d,n)
