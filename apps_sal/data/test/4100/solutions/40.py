N,K,Q=list(map(int,input().split()))
score=[K for _ in range(N)]
for _ in range(Q):
    A=int(input())
    score[A-1]+=1
for i in range(N):
    if score[i]-Q>0:
        print("Yes")
    else:
        print("No")

