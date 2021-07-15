N,K,Q = map(int,input().split())
A = [int(input()) for i in range(Q)]
B = [K]*N
p = 0
for i in range(Q):
    B[A[i]-1] += 1
for i in range(N):
    if(B[i] > Q):
        print("Yes")
    else:
        print("No")
