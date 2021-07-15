N,M=map(int,input().split())
PY=[list(map(int,input().split())) for i in range(M)]
PYI=sorted([(p,y,i) for i,(p,y) in enumerate(PY)])
r=['']*M
a,b=0,0
for p,y,i in PYI:
    if a!=p:
        a,b=p,1
    else:
        b+=1
    r[i]=str(p).zfill(6)+str(b).zfill(6)
print(*r,sep='\n')
