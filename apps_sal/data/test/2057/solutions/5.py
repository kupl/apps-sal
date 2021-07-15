n = int(input())
a = [int(i) for i in input().split()]
vis = [False] * n
ans = 0
for i in range(n):
    if a[i] == 0:
        ans += 1
        vis[0] = True
    elif vis[a[i]]:
        ans += 1
    else:
        vis[a[i]] = True
print(ans)
