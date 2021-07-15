n = int(input())
B = list(map(int, input().split()))

A = [0]*n
A[0] = B[0]
A[n-1] = B[n-2]

if n >= 3:
    for i in range(1, n-1):
        A[i] = min(B[i], B[i-1])

print((sum(A)))

