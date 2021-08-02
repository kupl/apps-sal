A = list(map(int, input().split()))
A.sort()
if A[0] + A[1] + A[2] == A[3] or A[0] + A[3] == A[1] + A[2]:
    print('Yes')
else:
    print('No')
