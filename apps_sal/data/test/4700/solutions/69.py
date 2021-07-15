n,m = map(int,input().split())
h = list(map(int,input().split()))
la = [0] * n
for i in range(m):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    la[a] = max(la[a],h[b])
    la[b] = max(la[b],h[a])

ans = 0
    
for i in range(n):
    if la[i] < h[i]:
        ans += 1
        
print(ans)
