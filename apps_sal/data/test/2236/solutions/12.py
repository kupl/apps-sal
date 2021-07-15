n=int(input())
L=[int(x) for x in input().split()]
a=0
d={}
for i in L:
    a+=i
    if a not in d:
        d[a]=0
    d[a]+=1
print(n-max(d.values()))

