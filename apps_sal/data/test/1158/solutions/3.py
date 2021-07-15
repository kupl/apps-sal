n,k=list(map(int,input().split()))
a=list(map(int,input().split()))
import collections
b=collections.Counter(a)
#print(b)
c=b.most_common(1)[0][1]
gg=max((c+k-1)//k,1)
need=k*gg*len(b)
#print(c)

for i in b:
    need-=b[i]
    


print(need)

