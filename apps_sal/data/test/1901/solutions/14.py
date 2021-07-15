import sys, threading
sys.setrecursionlimit(100010)
threading.stack_size(67108864)
#sys.stdin=open("input.txt","r")


def main():
    n,m=list(map(int,input().split()))
    c=list(map(int,input().split()))
    edge=[[] for i in range(n)]
    for i in range(m):
        u,v=list(map(int,input().split()))
        u-=1
        v-=1
        edge[u].append(v)
        edge[v].append(u)
    flag=[0]*n

    def dfs(u,k):
        flag[u]=k;
        for v in edge[u]:
            if(flag[v]==0):
                dfs(v,k)

    cnt = 0
    for u in range(n):
        if(flag[u]==0):
            cnt+=1
            dfs(u,cnt)

    mn=[0x3f3f3f3f]*(cnt+1)

    for u in range(n):
        mn[flag[u]]=min(mn[flag[u]],c[u])

    print(sum(mn[1:]))

thread=threading.Thread(target=main)
thread.start()



