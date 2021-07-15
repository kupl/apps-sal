n=int(input())
q=input()
c=list(q)
r=0
g=0
b=0
t=0
for i in range(0,len(c)) :
    if c[i]=="R" :
        r=r+1
        g=0
        b=0
    elif c[i]=="G" :
        r=0
        g=g+1
        b=0
    else :
        r=0
        g=0
        b=b+1
    if r>1 :
        t=t+1
        r=1
    if g>1 :
        t=t+1
        g=1
    if b>1 :
        t=t+1
        b=1
print(t)

