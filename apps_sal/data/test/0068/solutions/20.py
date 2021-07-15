def go(pos,k):
    if 'U'==k:
        pos[1]+=1
    elif 'D'==k:
        pos[1]-=1
    elif 'L'==k:
        pos[0]-=1
    else:
        pos[0]+=1
    return pos

def relapos(a,b):           #返回b的坐标减a的坐标
    c=[b[0]-a[0],b[1]-a[1]]
    return c

def stdis(a,b):
    return abs(b[1]-a[1])+abs(b[0]-a[0])
    

n=int(input())
s=input()
x,y=[int(i) for i in input().split()]
poss=[[0,0]]             #第n次操作后的位置
pos=[0,0]
for i in range(0,n):
    poss.append(tuple(go(pos,s[i])))
if abs(x)+abs(y)>n or abs(n-x-y)%2!=0:
    print(-1)
else:
    lpos=poss[-1]
    dd=stdis(lpos,[x,y])
    if dd==0:
        print(0)
    else:
        q1=(dd-1)//2
        q2=n
        j=True
        lpos1=[0,0]
        while q2-q1!=1:
            q=(q2+q1)//2
            for k1 in range(n-q+1):
                r=relapos(poss[k1],poss[k1+q])
                lpos1[0]=lpos[0]-r[0]
                lpos1[1]=lpos[1]-r[1]
                if stdis(lpos1,[x,y])<=q:
                    q2=q
                    break
            else:
                q1=q
        print(q2)

