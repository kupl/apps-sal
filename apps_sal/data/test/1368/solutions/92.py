N,A,B=list(map(int,input().split()))
l=list(map(int,input().split()))
l.sort(reverse=True)
all_n=l.count(l[0])
from scipy.special import comb
from collections import Counter
l2=l[0:A]
l_c=Counter(l)
max_mean=sum(l2)/A
l2=Counter(l2).items()
print(max_mean)
ans=1
if l[0]==l[A-1]:
   ans=0
   for i in range(A,B+1):
      ans+=comb(all_n,i,exact=True)
   print(ans)
   return
for i,j in l2:
   ans*=comb(l_c[i],j,exact=True)
print(ans)
