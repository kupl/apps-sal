import itertools
K=int(input())
X,Y=list(map(int,input().split()))
Mdist=abs(X)+abs(Y)
if Mdist%2==1 and K%2==0:
    print((-1))
    return
    #K:偶数ならマンハッタン距離が偶数の点にしか行けない
    #逆にKが偶数ならマンハッタン距離が偶数の任意の点に行ける
    #K:奇数なら理論上どこでも行ける
    #よってこれ以外のパターンは全部可能
    #(0,0)->(2n+1,0)->(n+1,n+1)->(1,0)
#K:奇数のとき、移動回数と距離がmod2 で合同
def searcheven(x,y):
    if abs(x)+abs(y)>2*K:
        return None
    if (abs(x)+abs(y))%2==1:
        return None
    for ps in itertools.product([-1,1],repeat=4):
        p1,p2,p3,p4=ps
        if p1*p4==p2*p3:
            if p3*(K-p1*x-p2*y)==-p1*K:
                a,b=0,p4*K
                if abs(x-a)+abs(y-b)==K and abs(a)+abs(b)==K:
                    return (a,b)
                a,b=p3*K,0
                if abs(x-a)+abs(y-b)==K and abs(a)+abs(b)==K:
                    return (a,b)
            else:
                pass
        else:
            tmp1=K-p1*x-p2*y
            tmp2=K
            tmp3=p4*tmp1+p2*tmp2
            tmp4=-p3*tmp1-p1*tmp2
            det=-p1*p4+p2*p3
            a,b=(tmp3//det,tmp4//det)
            if abs(x-a)+abs(y-b)==K and abs(a)+abs(b)==K:
                return (a,b)
            else:
                pass
    return None

ans=[(0,0)]
while(True):
    nx,ny=ans[-1]
    if abs(nx-X)+abs(ny-Y)<=2*K:
        if (abs(nx-X)+abs(ny-Y))%2==0:
            p,q=searcheven(X-nx,Y-ny)
            ans.append((p+nx,q+ny))
            ans.append((X,Y))
            break
        else:
            if abs(nx-X)+abs(ny-Y)==K:
                ans.append((X,Y))
                break
            tmpx=K//2
            tmpy=K-tmpx
            nextkouho=[(tmpx,tmpy),(tmpx,-tmpy),(-tmpx,tmpy),(-tmpx,-tmpy),(K,0),(-K,0),(0,K),(0,-K)]
            for point in nextkouho:
                ptmp,qtmp=point
                p=ptmp+nx;q=qtmp+ny
                if abs(X-p)+abs(Y-q)<=2*K:
                    ans.append((p,q))
                    break
    elif abs(nx)+K<=abs(X):
        if X<0:
            ans.append((nx-K,ny))
            continue
        else:
            ans.append((nx+K,ny))
            continue
    elif abs(ny)+K<=abs(Y):
        if Y<0:
            ans.append((nx,ny-K))
            continue
        else:
            ans.append((nx,ny+K))
            continue


#print(ans)
s=len(ans)-1
flag=1
for i in range(s):
    ax,ay=ans[i]
    bx,by=ans[i+1]
    if abs(ax-bx)+abs(ay-by)==K:
        pass
    else:
        flag=0
        break
if flag==0:
    print("NG")
print(s)
for i in range(1,s+1):
    print((ans[i][0],ans[i][1]))

