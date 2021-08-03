N, A, B = list(map(int, input().split()))

x = N // (A + B)
y = N % (A + B)

if y <= A:
    print((str(A * x + y)))
else:
    print((str(A * x + A)))
