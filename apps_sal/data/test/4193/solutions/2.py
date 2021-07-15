A = [list(map(int, input().split())) for i in range(3)]
N = int(input())
B = [0 for i in range(8)]
for i in range(N):
    b = int(input())
    if b == A[0][0] or b == A[1][0] or b == A[2][0]:
        B[0] += 1
    if b == A[0][1] or b == A[1][1] or b == A[2][1]:
        B[1] += 1
    if b == A[0][2] or b == A[1][2] or b == A[2][2]:
        B[2] += 1
    if b == A[0][0] or b == A[0][1] or b == A[0][2]:
        B[3] += 1
    if b == A[1][0] or b == A[1][1] or b == A[1][2]:
        B[4] += 1
    if b == A[2][0] or b == A[2][1] or b == A[2][2]:
        B[5] += 1
    if b == A[0][0] or b == A[1][1] or b == A[2][2]:
        B[6] += 1
    if b == A[0][2] or b == A[1][1] or b == A[2][0]:
        B[7] += 1
if 3 in B:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)
