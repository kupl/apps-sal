N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

B.insert(0, 0)
C.insert(0, 0)
satis = 0
tmp = 999
for i in range(N):
    satis += B[A[i]]
    if (tmp - A[i]) == -1:
        satis += C[tmp]
    tmp = A[i]
print(satis)
