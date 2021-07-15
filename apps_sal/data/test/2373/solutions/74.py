n=int(input())
c=list(map(int, input().split()))
ans = 0

for i in range(n-1):
    if c[i] == i+1 :
        c[i],c[i+1]= c[i+1],c[i]
        ans += 1
if c[n-1] == n:
    ans += 1
print(ans)
