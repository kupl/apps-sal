A, B, C, K = list(map(int, input().split()))

if K <= A:
    x = K
elif A < K <= A + B:
    x = A
else:
    x = A - (K - A - B)

print(x)
