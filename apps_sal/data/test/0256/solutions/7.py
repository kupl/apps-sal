mtr=[[1,0],[0,1]]
p1=list(map(int,input().split()))
p2=list(map(int,input().split()))
p3=list(map(int,input().split()))
p4=list(map(int,input().split()))
w1=w2=0
for l1 in mtr:
    wi1=wi2=0
    for l2 in mtr:
        at1=p1[1] if l1[0]==1 else p2[1]
        z1=p1[0] if l1[0]==0 else p2[0]
        at2=p3[1] if l2[0]==1 else p4[1]
        z2=p3[0] if l2[0]==0 else p4[0]
        if at1>z2 and z1>at2:
            wi1+=1
        elif at1<z2 and z1<at2:
            wi2+=1
    if wi2>=1:
        w2+=1
    elif wi1==2:
        w1+=1
if w2==2:
    print('Team 2')
elif w1>=1:
    print('Team 1')
else:
    print('Draw')

