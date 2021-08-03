A, B, C, K = list(map(int, input().split()))
R = A + B
if K < A:
    print(K)
elif K <= R:
    print(A)
else:
    T = K - R
    print((A - T))
