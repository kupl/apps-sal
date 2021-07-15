n=int(input())
P=list(map(int,input().split()))
ans=0
for i in range(1,n-1):
  if sorted([P[i-1],P[i],P[i+1]]).index(P[i]) == 1:
    ans += 1
print(ans)
