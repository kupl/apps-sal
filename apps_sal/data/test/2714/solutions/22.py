import sys
from collections import defaultdict, deque
mod = 998244353


def get(graph):
    vis = defaultdict(int)
    l = []
    for i in range(1, n + 1):
        if vis[i] == 0:
            vis[i] = 1
            q = deque()
            q.append(i)
            even = 0
            odd = 0
            while q:
                a = q.popleft()
                if vis[a] & 1:
                    odd += 1
                else:
                    even += 1
                for x in graph[a]:
                    if vis[x] == 0:
                        if vis[a] == 1:
                            vis[x] = 2
                        else:
                            vis[x] = 1
                        q.append(x)
                    elif vis[x] == vis[a]:
                        return 0
            l.append([even, odd])
    m = len(l)
    x = pow(2, l[0][0], mod)
    y = pow(2, l[0][1], mod)
    ans = (x + y) % mod
    for i in range(1, m):
        x = pow(2, l[i][0], mod)
        y = pow(2, l[i][1], mod)
        z = (x + y) % mod
        ans = ans * z
        ans %= mod
    return ans % mod
    return False


'def count(graph):\n    vis=defaultdict(int)\n    even=0\n    odd=0\n    for i in range(1,n+1):\n        if vis[i]==0:\n            vis[i]=1\n            q=deque()\n            q.append([i,0])\n            while q:\n                a,dis=q.popleft()\n                if dis%2==0:\n                    even+=1\n                else:\n                    odd+=1\n                for x in graph[a]:\n                    if vis[x]==0:\n                        vis[x]=1\n                        q.append([x,dis+1])\n    return (even,odd)'
t = int(sys.stdin.readline())
for _ in range(t):
    graph = defaultdict(list)
    (n, m) = list(map(int, sys.stdin.readline().split()))
    for i in range(m):
        (u, v) = list(map(int, sys.stdin.readline().split()))
        graph[u].append(v)
        graph[v].append(u)
    "if _ == 5:\n        print(graph)\n    #print(graph,'graph')"
    z = get(graph)
    print(z)
