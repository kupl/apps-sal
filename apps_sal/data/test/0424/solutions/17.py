x = int(input())
n = x
vis = [False for i in range(n+1)]
flag = [0 for i in range(n+1)]
for i in range(2, n+1):
    if not vis[i]:
        for j in range(i+i, n+1, i):
            vis[j] = True
            flag[j] = i
ans = x
for i in range(x - flag[x] + 1, x+1):
    ans = min(ans, i - flag[i] + 1)
print(ans)

