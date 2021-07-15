N=int(input())
MOD=1000000007
A=list(map(int,input().split()))
cnt=[0 for i in range(N)]
for i in range(N):
    cnt[A[i]]+=1
if N%2==0:
    for i in range(1,N,2):
        if cnt[i]!=2:
            print((0))
            break
    else:
        print((2**(N//2)%MOD))
else:
    if cnt[0]!=1:
        print((0))
    else:
        for i in range(2,(N+1)//2,2):
            if cnt[i]!=2:
                print((0))
                break
        else:
            print((2**((N-1)//2)%MOD))

