n = int(input())
a = list(map(int,input().split()))
ans = a[0] * (n-a[0]+1)
for i in range(1, n):
    if a[i-1] == a[i]: continue
    elif a[i-1] < a[i]: ans+= (a[i]-a[i-1]) * (n-a[i]+1)
    elif a[i-1] > a[i]: ans+= a[i] * (a[i-1]-a[i])
print(ans)
