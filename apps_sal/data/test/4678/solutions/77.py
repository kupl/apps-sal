n = int(input())
a = list(map(int,input().split()))
ans = 0
x = a[0]
for i in range(n):
    x = max(x,a[i])
    if a[i]<x:
        ans+=x-a[i]
print(ans)
