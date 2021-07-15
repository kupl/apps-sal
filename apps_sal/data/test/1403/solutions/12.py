n,k = list(map(int,input().split()))
ai = list(map(int,input().split()))
ai.sort()
last = ai[n-1]
ans = 1
lastAlive = ai[n-1]
for i in range(n-2,-1,-1):
    if last - k > ai[i] or lastAlive == ai[i]:
        ans += 1
        lastAlive = ai[i]
    last = ai[i]
print(ans)

