(A, B, N) = list(map(int, input().split()))
if B <= N:
    a = int(A * (B - 1) / B)
    b = 0
    print(max(a, b))
else:
    a = int(A * N / B)
    b = 0
    print(max(a, b))
