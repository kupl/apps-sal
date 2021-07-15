N = int(input())
A = list(map(int, input().split()))
B = A.copy()
ans = [0, 0]
flag1 = True
flag2 = False
for i in range(0, N):
    if i != 0:
        A[i] += A[i-1]
    if flag1:
        if A[i] <= 0:
            ans[0] += (abs(A[i])+1)
            A[i] = 1
        flag1 = False
    else:
        if A[i] >= 0:
            ans[0] += (abs(A[i])+1)
            A[i] = -1
        flag1 = True
for i in range(0, N):
    if i != 0:
        B[i] += B[i-1]
    if flag2:
        if B[i] <= 0:
            ans[1] += (abs(B[i])+1)
            B[i] = 1
        flag2 = False
    else:
        if B[i] >= 0:
            ans[1] += (abs(B[i])+1)
            B[i] = -1
        flag2 = True
print((min(ans)))

