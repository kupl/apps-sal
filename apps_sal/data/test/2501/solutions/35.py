from collections import Counter

n=int(input())
a=list(map(int,input().split()))

l1=[i+a[i] for i in range(n)]
l2=[i-a[i] for i in range(n)]

c1=Counter(l1)
c2=Counter(l2)

ans=0
for i in c1:
  ans+=c1[i]*c2[i]

print(ans)
