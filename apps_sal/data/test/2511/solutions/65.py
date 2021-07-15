import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
MOD = 10**9+7
N,K = map(int,input().split())
edge = [[] for _ in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

ans = 1
def dfs(now, par,num):
    nonlocal ans
    ans = ans*num%MOD
    num = K-1
    if par != -1:
        num -= 1
    for ch in edge[now]:
        if ch != par:
            dfs(ch,now,num)
            num -= 1

dfs(0,-1,K)
print(ans)
