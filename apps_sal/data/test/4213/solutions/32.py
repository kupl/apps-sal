N = int(input())
A = [int(i) for i in input().split()]

A = sorted(A)
print(A[-1] - A[0])
