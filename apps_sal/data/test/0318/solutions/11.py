h,m=list(map(int,input().split(':')))
a=int(input())


h+=((m+a)//60)
m=(m+a)%60
h%=24

ms=""
hs=""
if(h<10):
    hs+="0"
if(m<10):
    ms+="0"
hs+=str(h)
ms+=str(m)
print("%s:%s"%(hs,ms))

