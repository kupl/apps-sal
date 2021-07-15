n = int(input())
A = sorted([int(i) for i in input().split()])
if A[n] > A[n-1]:
    print('YES')
else:
    print('NO')


