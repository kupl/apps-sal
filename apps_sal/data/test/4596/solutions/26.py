N=int(input())
A=list(map(int,input().split()))
def rec(A):
    B=[0]*N
    for i in range(N):
        if A[i] % 2 != 0: return 0
        B[i] = A[i] / 2
    return rec(B)+1
print(rec(A))
