import collections
N=int(input())
a=list(map(int,input().split()))
c=collections.Counter(a)
ans=0
for i,j in c.items():
  if i>j:
    ans+=j
  elif j>i:
    ans += j-i
print(ans)
