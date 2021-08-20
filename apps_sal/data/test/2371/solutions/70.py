(n, z, w) = map(int, input().split())
A = list(map(int, input().split()))
if n == 1:
    print(abs(A[0] - w))
else:
    z1 = A[-1]
    w1 = A[-2]
    print(max(abs(z1 - w), abs(z1 - w1)))
