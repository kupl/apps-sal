import sys

n = int(input())
A = [0]*(2*n)
B = []
for line in sys.stdin:
    x, y = [int(x)-1 for x in line.split()]
    A[x] = y
    A[y] = x
    B.append(x)

C = [0]*(2*n)
for i in range(2*n):
    while not C[i]:
        C[i] = 1
        C[i^1] = 2
        i = A[i^1]

for x in B:
    print(C[x], C[A[x]])

