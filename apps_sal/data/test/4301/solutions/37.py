N = int(input())
A = [int(input()) for i in range(N)]
I1 = A.index(max(A))
M1 = A.pop(I1)
M2 = max(A)
for j in range(N):
    if j == I1:
        print(M2)
    else:
        print(M1)
