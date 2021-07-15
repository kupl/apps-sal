A, B, C, K = list(map(int, input().split()))

if K <= A:
    print(K)
elif A < K <= A + B:
    print(A)
elif A + B < K <= A + B + C:
    print((2*A+B-K))

