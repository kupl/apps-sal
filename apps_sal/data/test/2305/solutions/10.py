import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
C = list(map(int,input().split()))

path = [set() for _ in range(n)]

for i in range(n-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    path[a].add(b)
    path[b].add(a)
    
ans = [n*(n+1)//2]*n
size = [0]*n
cparent = [[] for _ in range(n)]
reached = [False]*n
root_size = [n]*n

def dfs (p):
    c = C[p] - 1
    cparent[c].append(p)
    s = 1
    for nxt in path[p]:
        #print (nxt)
        
        if reached[nxt]:
            continue
        size[p] = 0
        reached[nxt] = True
        ret = dfs(nxt)
        s += ret
        size[p] +=ret
        ans[c] -= size[p] * (size[p] + 1)//2
    cparent[c].pop()
    if cparent[c]:
        size[cparent[c][-1]] -=s
    else:
        root_size[c] -=s    
    return s

reached[0] = True
dfs (0)

for i in range(n):
    print (ans[i]-root_size[i]*(root_size[i]+1)//2)
