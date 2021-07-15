N=int(input())
A=list(map(int,input().split()))
cnt=[0 for i in range(N)]
for i in range(N-1):
    cnt[A[i]-1]+=1
for i in range(N):
    print((cnt[i]))

