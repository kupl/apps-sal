N,M=map(int,input().split())
A=[]
for i in range(M):
    P,Y=map(int,input().split())
    A.append([P,Y,i])

ans=[""]*M
A=sorted(A, key=lambda x: x[1])
A=sorted(A,key=lambda x:x[0])

now=A[0][0]
cnt=1
for i in range(M):
    pref=str(A[i][0])
    
    if A[i][0]!=now:
        cnt=1
    year=str(cnt)
    now=A[i][0]
    cnt+=1

    ans[A[i][2]]=pref.zfill(6)+year.zfill(6)

for i in range(M):
    print(ans[i])
