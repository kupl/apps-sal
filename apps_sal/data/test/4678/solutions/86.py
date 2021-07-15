n =int(input())
l = list(map(int, input().split()))
ans=0
for i in range(1,n):
    if l[i-1] > l[i]:
        ans +=l[i-1] - l[i]
        l[i] =l[i-1]
print(ans)
