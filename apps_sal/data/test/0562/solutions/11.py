from operator import itemgetter
n = int(input())
A = []
for i in range(n):
    A.append([int(i) for i in input().split()])
A = sorted(A, key=itemgetter(0))
first_tv = []
second_tv = []
first_end = -1
second_end = -1
for i in range(n):
    if A[i][0] > first_end:
        first_end = A[i][1]
    elif A[i][0] > second_end:
        second_end = A[i][1]
    else:
        print('NO')
        break
else:
    print('YES')
