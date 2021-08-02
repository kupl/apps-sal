N = int(input())
A = list(map(int, input().split()))

A.sort()

print(A[-1] - A[0] if N > 1 else 0)
