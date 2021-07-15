n = int(input())
s = [0]*n
g = [0]*n
for i in range(n):
    a,b = list(map(int,input().split()))
    s[i] = a
    g[i] = a+b

for i in range(1,n):
    g[i] = min(g[i],g[i-1]+1)
for i in range(n-2,-1,-1):
    g[i] = min(g[i],g[i+1]+1)

ans = 0
for i in range(n):
    if s[i] <= g[i]:
        ans += g[i] - s[i]
    else:
        print(-1)
        break

else:
    print(ans)
    print(*g)

