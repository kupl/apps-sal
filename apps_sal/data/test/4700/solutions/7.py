N,M=list(map(int,input().split()))
H=list(map(int,input().split()))
cnt=[1 for _ in range(N)]
for _ in range(M):
    A,B=list(map(int,input().split()))
    A-=1
    B-=1
    if H[A]>H[B]:
        cnt[B]=0
    elif H[A]<H[B]:
        cnt[A]=0
    else:
        cnt[A]=0
        cnt[B]=0
print((cnt.count(1)))

