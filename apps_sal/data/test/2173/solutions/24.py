n=int(input())
lst=[*map(int,input().split())]
ind=sorted(range(n),key=lst.__getitem__)
elem=0
for i,x in enumerate(ind):
    elem=max(elem+1,lst[x])
    lst[x]=elem
print(*lst)
