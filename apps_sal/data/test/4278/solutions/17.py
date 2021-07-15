import collections 
from scipy.special import comb

N=int(input())
List=[]
for i in range(N):
    line=list(str(input()))
    line.sort()
    List.append("".join(line))
 
ans=0   
for i,j in collections.Counter(List).items():
    num=comb(j, 2, exact=True)
    ans+=num
    
print(ans)
