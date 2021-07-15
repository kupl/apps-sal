import sys 
sys.setrecursionlimit(10**6)
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N,u,v = list(map(int,readline().split()))
AB = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = list(map(int,readline().split()))
    AB[a].append(b)
    AB[b].append(a)
    
tdist = [0]*(N+1)
adist = [0]*(N+1)

def tdfs(x,pre):
    for to in AB[x]: 
        if to == pre:
            continue
        tdist[to] = tdist[x]+1
        tdfs(to,x)

def adfs(x,pre):
    for to in AB[x]: 
        if to == pre:
            continue
        adist[to] = adist[x]+1
        adfs(to,x)

tdfs(u,-1)
adfs(v,-1)

ans = 0
for i in range(1,N+1):
    if tdist[i] < adist[i]:
        k = adist[i] - tdist[i]
        ans = max(ans,tdist[i] + k-1)
print(ans)

