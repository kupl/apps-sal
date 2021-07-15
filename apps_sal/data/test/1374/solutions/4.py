n=int(input())
a=list(map(int,input().split()))
a2=sorted(set(a))
L=len(a2)
if n==1:print(a[0]);return
elif n==2:print(a[1]);return
ng=L
ok=0
while ng-ok>1:
    check=a2[(ok+ng)//2]
    cnt=0 #check以上の要素の数
    idx=n
    cl=[0]*(2*n+1)
    cl[n]=1
    Ru=0
    for i in range(n):
        if a[i]<check:
            Ru-=cl[idx]-1
            idx-=1
        else:
            idx+=1
            Ru+=cl[idx]+1
        cnt += Ru
        cl[idx]+=1
    if cnt >= ((n+1)*n//2)//2:
        ok = (ok+ng)//2
    else:
        ng = (ok+ng)//2
print(a2[ok])
