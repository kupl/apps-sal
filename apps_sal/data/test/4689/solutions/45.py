k, n = map(int ,input().split())
a = list(map(int,input().split()))

a.append(k+a[0])

d = 0
ans = 0
for i in range(n):
    d = (a[i+1]-a[i])
    ans =max(ans,d)
    
print(k-ans)
