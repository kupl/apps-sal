from collections import defaultdict
d=defaultdict(int)
N=int(input())
a=list(map(int,input().split()))
for x in a:
    d[x]+=1
    d[x-1]+=1
    d[x+1]+=1
print(max(d.values()))
