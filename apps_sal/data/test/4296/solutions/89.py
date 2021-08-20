A = [int(i) for i in input().split()]
if A[0] + A[1] + A[2] >= 22:
    print('bust')
if A[0] + A[1] + A[2] < 22:
    print('win')
