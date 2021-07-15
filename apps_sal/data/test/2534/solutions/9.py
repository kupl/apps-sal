from numpy import *
r,c=map(int,input().split())
x=[]
for i in range(r):
    y=list(map(int,input().split()))
    x.append(y)
x=array(x)
b=x.transpose()
for i in x:
    c=[]
    i=list(i)
    a=min(i)
    ab=0
    for k in range(len(i)):
        if(i[k]==a):
            c.append(k)
    for k in c:
        d=max(list(b[k]))
        if(a==d):
            print(a)
            ab+=1
            break
    if(ab>0):
        break
else:
    print("GUESS")
