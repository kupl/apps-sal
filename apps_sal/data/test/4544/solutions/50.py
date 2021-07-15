n=int(input())
a=list(map(int, input().split()))
ans = 0
l = [0]*(10**5+2)
for i in range(n):
    l[a[i]] +=1
for i in range(10**5):
    x = l[i] +l[i+1]+l[i-1]
    ans = max(ans,x)
print(ans)
