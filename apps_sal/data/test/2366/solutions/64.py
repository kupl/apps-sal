from collections import Counter
n=int(input())
A=list(map(int,input().split()))
cnt=Counter(A)
tot=0
dif={}
for k,v in cnt.items():
  tot += v*(v-1)//2
  dif[k]=v-1
ans=[tot-dif[a] for a in A]
print('\n'.join(map(str,ans)))
