n = int(input()); arr = [list(map(int,input().split())) for _ in range(n-1)]

graph = [[] for _ in range(n)]
for a,b in arr:
    graph[a-1].append(b-1); graph[b-1].append(a-1)

parents = [-1]*n
children = [[] for _ in range(n)]
orders = []
stack = [0]
flags = [True] * n; flags[0] = False
while stack:
    tmp = stack.pop()
    orders.append(tmp)
    for node in graph[tmp]:
        if flags[node]:
            flags[node] = False
            children[tmp].append(node)
            stack.append(node)
            parents[node] = tmp

mod = 10**9+7
fac = [1]*(n+1)
inv = [1]*(n+1)
ifac = [1]*(n+1)
for i in range(2,n+1):
    fac[i] = fac[i-1] * i % mod
    inv[i] = (- (mod//i)*inv[(mod%i)]) % mod
    ifac[i] = ifac[i-1] * inv[i] % mod

size = [1] * n;dp = [1] * n
for parent in orders[::-1]:
    for child in children[parent]:
        size[parent] += size[child]
        dp[parent] = dp[parent] * dp[child] * ifac[size[child]] % mod
    dp[parent] = dp[parent] * fac[size[parent]-1] % mod

size2 = [n-i+1 for i in size];dp2 = [1] * n; dp2[0] = dp[0]
for parent in orders[1:]:
    child = parents[parent]
    dp2[parent] = dp2[parent] * size[parent] * dp2[child] * inv[size2[parent]-1] % mod
    
for i in range(n):
    print(dp2[i])
