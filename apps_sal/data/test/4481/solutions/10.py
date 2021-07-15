import collections
N=int(input())
S=[]
for i in range(N):
  s=input()
  S.append(s)

l=collections.Counter(S)
keys=l.keys()
k=max(l.values())
ans=[]
for i in keys:
  if l[i]==k:
    ans.append(i)

ans.sort()
n=len(ans)

for i in range(n):
  print(ans[i])
