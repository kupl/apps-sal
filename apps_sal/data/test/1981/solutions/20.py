from collections import deque

n,m = list(map(int,input().split()))
cat =[0] + list(map(int,input().split()))
path = [0] + [set() for _ in range(n)]
dp = [0] * (n+1)
for _ in range(n-1):
    x, y = list(map(int , input().split()))
    path[x].add(y)
    path[y].add(x)

d = deque()

d.append(1)
dp[1] = cat[1]
ans = 0
while len(d) > 0:
    t = d.popleft()
    if dp[t] > m :
        continue
    if len(path[t]) == 0:
        if dp[t] <= m:
            ans+=1
    for x in path[t]:
        path[x].remove(t)
        d.append(x)
        if cat[x] != 0:
            dp[x] = dp[t] + cat[x]
        else:
            dp[x] = 0

print(ans)

