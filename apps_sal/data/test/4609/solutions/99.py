import collections
n=int(input())
a=[int(input()) for _ in range(n)]
b=collections.Counter(a)
ans=0
for i in b.keys():
  if b[i]%2:
    ans+=1
print(ans)
