N=int(input())
C=input()


rw=C.count('R')
wr=0
ans=rw

for i in range(N):
    if C[i]=='R':
        rw-=1
    else:
        wr+=1
    ans=min(ans,max(rw,wr))
print(ans)
