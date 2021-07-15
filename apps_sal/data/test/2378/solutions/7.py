#f
import sys
sys.setrecursionlimit(2 * 10 ** 5 + 10)
 

n = int(input())
E = [[] for _ in range(n)]
mod = 10**9 + 7

for i in range(n-1):
    a,b = [int(x) for x in input().split()]
    E[a-1].append((b-1, i)) 
    E[b-1].append((a-1, i)) 
    
X = [0] * n
    
def dfs(u,e):
    num = 1
    for v,c in E[u]:
        if c != e:
            num += dfs(v,c)
    X[e] = num 
    return num

dfs(0, -1)

I = [1]
inv = pow(2, mod-2, mod)
for i in range(n):
    I.append(I[-1] * inv % mod)

ans = 0
for i in range(n):
    x = X[i]
    ans += (1-I[x])*(1-I[n-x]) % mod
    
ans -= n * I[1]
ans += 1 - I[n]
ans %= mod
print(ans)


