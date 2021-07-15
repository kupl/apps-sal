N,M=list(map(int,input().split()))
cnt=[0 for _ in range(M)]
for _ in range(N):
    A=list(map(int,input().split()))
    for j in range(1,A[0]+1):
        cnt[A[j]-1]+=1
print((cnt.count(N)))

