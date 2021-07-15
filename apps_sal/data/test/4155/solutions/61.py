n = int(input())
h = list(map(int,input().split()))
h.append(101)
ans = 0
start = 0
i = 0
while sum(h[:n])!=0:
    if h[i]!=0:
        h[i] -= 1
    if h[i]==0:
        start = i+1    
    if h[i]>=h[i+1] or i==n-1:
        ans += 1
        i = start
        continue
    i += 1
print(ans)
