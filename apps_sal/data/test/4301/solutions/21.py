import copy
n = int(input())
A = []
for i in range(n):
    A.append(int(input()))
B = copy.copy(A)
B.sort()
A_max = B[-1]
A_max2 = B[-2]

for i in range(n):
    if A[i] < A_max:
        print(A_max)
    elif A[i] == A_max:
        print(A_max2)
