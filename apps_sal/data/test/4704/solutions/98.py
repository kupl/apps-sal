n=int(input())
a=[int(x) for x in input().rstrip().split()]

ruiseki=[0]
for i in range(n):
  ruiseki.append(ruiseki[i]+a[i])

ans=float('inf')
last=ruiseki[len(ruiseki)-1]
# print(last)
# print(ruiseki)
for i in range(1,len(ruiseki)-1):
  now=(last-ruiseki[i])
  ans=min(ans,abs(ruiseki[i]-now))
print(ans)
  



