import collections
n=int(input())
a=[0]*n
ans=0
for i in range(n):
    a[i]=input()
c=collections.Counter(a)
l=list(set(a))
for i in range(len(l)):
    if c[l[i]]%2==1:
        ans+=1
print(ans)
