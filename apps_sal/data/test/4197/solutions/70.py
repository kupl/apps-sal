N=int(input())
Alist=list(map(int,input().split()))
index=[i+1 for i in range(N)]
Adict=dict(zip(Alist,index))
for i in range(1,N+1):
    print(Adict[i],end=' ')
