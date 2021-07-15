"""
NTC here
"""
from sys import setcheckinterval,stdin,setrecursionlimit
setcheckinterval(1000)
setrecursionlimit(10**6)

#print("Case #{}: {} {}".format(i, n + m, n * m))

iin=lambda :int(stdin.readline())
lin=lambda :list(map(int,stdin.readline().split()))


from fractions import gcd
n=iin()
points=[lin() for i in range(n)]
ans=set()
for i in range(n):
    x1,y1=points[i]
    for j in range(i+1,n):
        x2,y2=points[j]
        a,b,c=y1-y2,x2-x1,y1*(x1-x2)-x1*(y1-y2)
        g=gcd(gcd(a,b),c) if c else gcd(a,b)

        ans.add((a//g,b//g,c//g))
intersections=set()
la=list(ans)
l=len(la)
for i in range(l):
    a,b,c=la[i]
    for j in range(i+1,l):
        try:
            e,d,f=la[j]
            y=(a*f-c*e)/(b*e-a*d)
            x=(c*d-b*f)/(b*e-a*d)
            intersections.add((i,j))
        except:
            pass
#print(intersections,ans,sep='\n')
print(len(intersections))
