from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(67108864)

def main():
    def dfs(v,cv):
        color[v]=cv
        for u in d[v]:
            if color[u]==0:
                dfs(u,cv)

    n,m=map(int,input().split())
    c=list(map(int,input().split()))
    d={x:[] for x in range(n+1)}
    for i in range(m):
        x,y=map(int,input().split())
        d[x].append(y)
        d[y].append(x)
    color=[0]*(n+1)
    cv=1
    for i in range(1,n+1):
        if color[i]==0:
            dfs(i,cv)
            cv+=1
    s={}
    for i in range(1,n+1):
        if color[i] in s:
            s[color[i]].append(c[i-1])
        else:
            s[color[i]]=[c[i-1]]
    x=0
    for i in s:
        x+=min(s[i])
    print(x)
thread = threading.Thread(target=main)
thread.start()
