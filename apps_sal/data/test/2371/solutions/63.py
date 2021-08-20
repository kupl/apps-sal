(n, z, w) = map(int, input().split())
A = list(map(int, input().split()))
if n == 1:
    print(abs(A[0] - w))
else:
    print(max(abs(A[-1] - w), abs(A[-2] - A[-1])))
