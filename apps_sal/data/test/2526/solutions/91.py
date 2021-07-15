x,y,a,b,c=list(map(int,input().split()))
p=[0]+sorted(list(map(int,input().split())))[a-x:]
q=[0]+sorted(list(map(int,input().split())))[b-y:]
r=[0]+sorted(list(map(int,input().split())))
pi=-1
qi=-1
ri=-1
gs=0
rs=0
ws=0
s=0              
while gs+rs+ws!=x+y:
    if r[ri]>=q[qi]>=p[pi]:
        s += r[ri]
        ws+=1
        ri-=1

    elif r[ri]>=p[pi]>=q[qi]:
        s += r[ri]
        ws += 1
        ri -= 1

    elif q[qi]>=r[ri]>=p[pi]:
        s += q[qi]
        gs += 1
        qi -= 1

    elif q[qi]>=p[pi]>=r[ri]:
        s += q[qi]
        gs += 1
        qi -= 1

    elif p[pi]>=r[ri]>=q[qi]:
        s += p[pi]
        rs += 1
        pi -= 1

    elif p[pi]>=q[qi]>=r[ri]:
        s += p[pi]
        rs += 1
        pi -= 1

print(s)

