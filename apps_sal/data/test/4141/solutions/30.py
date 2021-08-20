N = int(input())
A = []
A = [int(x) for x in input().split()]
for i in range(len(A)):
    if A[i] % 2 == 1:
        A[i] = 'YES'
    elif A[i] % 2 == 0 and A[i] % 3 != 0 and (A[i] % 5 != 0):
        A[i] = 'NO'
    else:
        A[i] = 'YES'
if 'NO' in A:
    print('DENIED')
else:
    print('APPROVED')
