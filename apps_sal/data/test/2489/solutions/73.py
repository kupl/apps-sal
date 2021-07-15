import collections as c
n,a1=int(input()),[*map(int,input().split())]
a2,a3,b=set(a1),c.Counter(a1),[0]*(10**6+1)
for i in a2:
  for j in range(i,10**6+1,i):
    b[j]+=1
print(sum(b[i]==1 and a3[i]==1 for i in a2))
