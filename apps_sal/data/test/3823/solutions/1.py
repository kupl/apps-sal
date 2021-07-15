from sys import *

s1=stdin.readline().strip()
n=int(s1)
s1=stdin.readline().strip()
a=list(map(float,s1.split()))


b=[]
for i in range (2*n):
    if int(a[i])!=a[i]:
        b.append(round(1000*(a[i]-int(a[i]))))
m=len(b)
r=0
for i in range (m):
    r=r+b[i]
if m<=n:
    if r>=1000*m:
        r=r-1000*m
    else:
        r=min(r-1000*(r//1000),1000-r+1000*(r//1000))
else:
    if r>=n*1000:
        r=r-1000*n
    else:
        if r<=1000*(m-n):
            r=1000*(m-n)-r
        else:
            r=min(r-1000*(r//1000),1000-r+1000*(r//1000))
r=r/1000
print("%.3f"%r)

