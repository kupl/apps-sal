N, Z, W = list(map(int, input().split()))
A = list(map(int, input().split()))

if N == 1:
    print((abs(A[0] - W)))
else:
    print((max(abs(A[-1] - W), abs(A[-1] - A[-2]))))
