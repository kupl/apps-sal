N=int(input())
A=[int(input()) for _ in range(N)]
B=sorted(A,reverse=True)
for i in range(N):
    if A[i]==B[0]:
        print(B[1])
    else:
        print(B[0])
