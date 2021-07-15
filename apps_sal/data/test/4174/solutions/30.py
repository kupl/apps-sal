r=input().split()
N=int(r[0])
X=int(r[1])
d=[int(s) for s in input().split()]
ans=1
le=0
for i in range(N):
    le+=d[i]
    if le>X:
        print(ans)
        break
    elif i==N-1:
        print(N+1)
    else:
        ans+=1
