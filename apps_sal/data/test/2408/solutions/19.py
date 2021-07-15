n=int(input().strip())
num=[]
for k in range(n):
    num.append(list(map(int,input().strip().split())))
d={}
import math
for k in range(n):
    for kk in range(k+1,n):
        a=num[k]
        b=num[kk]
        if(a[0]==b[0]):
            if((100000,100000) in d.keys()):
                d[(100000,100000)].add(a[0])
            else:
                d[(100000, 100000)]={a[0]}
        elif(a[1]==b[1]):
            if(0,1) in d.keys():
                d[(0,1)].add(a[1])
            else:
                d[(0,1)]={a[1]}
        else:
            c=b[1]-a[1]
            dd=b[0]-a[0]
            q=math.gcd(c,dd)
            c1=c//q
            d1=dd//q
            r=(a[0]*b[1])-(a[1]*b[0])
            if(r!=0):
                rr=math.gcd(r,dd)
                r=r//rr
                d2=dd//rr
                if(d2<0):
                    d2=-d2
                    r=-r
                if(d1<0):
                    d1=-d1
                    c1=-c1
                if((c1,d1) in d.keys() ):
                    d[(c1,d1)].add((r,d2))
                else:
                    d[(c1,d1)]={(r,d2)}
            else:
                if (d1 < 0):
                    d1 = -d1
                    c1 = -c1
                if ((c1, d1) in d.keys()):
                    d[(c1, d1)].add((0,1))
                else:
                    d[(c1, d1)] = {(0,1)}
s=0
for i in d.keys():
    s=s+(len(d[i]))
ss=0
for i in d.keys():
    s=s-(len(d[i]))
    ss=ss+(s*len(d[i]))
print(ss)
