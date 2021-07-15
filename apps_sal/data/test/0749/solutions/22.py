s=input()
n=len(s)
k=1
sim=set(s[0])
a=[0]*n
a[0]=1
sim=set(s)
d=dict()
for i in sim:
    d[i]=[-1,1]
for i in range(n):
    d[s[i]][1]=max(d[s[i]][1],i-d[s[i]][0])
    d[s[i]][0]=i
k=10000000
for i in list(d.values()):
    k=min(k,max(n-i[0],i[1]))
print(k)

