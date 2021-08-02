N = int(input())
A = [int(input()) for _ in range(N)]

M = max(A)
M_index = A.index(M)
sub_M = 0
for i in range(N):
    if i != M_index:
        sub_M = max(sub_M, A[i])

for i in range(N):
    if i == M_index:
        print(sub_M)
    else:
        print(M)
