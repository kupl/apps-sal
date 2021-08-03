A = list(map(int, input().split()))
A.sort()
a = abs(A[0] - A[1])
b = abs(A[1] - A[2])

print(a + b)
