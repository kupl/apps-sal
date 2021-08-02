N = int(input())
A = list(map(int, input().split()))

neg = sum(A[i] < 0 for i in range(len(A)))
if 0 in A or N % 2 == 1:
    neg = 0

B = sorted([abs(A[i]) for i in range(len(A))])
if neg & 1:
    print(- abs(B[0]) + sum(B[i] for i in range(1, len(B), 1)))
else:
    print(sum(B[i] for i in range(len(B))))
