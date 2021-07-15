n=int(input())
a=[int(x) for x in input().split()]
a=sorted(a)
l=len(a)
a1=[]
a2=[]
for i in range(1,n,2):
    a1.append(i)
for i in range(2,n+1,2):
    a2.append(i)
s1=0
s2=0
for i in range(l):
    s1=s1+abs(a1[i]-a[i])
for i in range(l):
    s2=s2+abs(a2[i]-a[i])
print(min(s1,s2))

