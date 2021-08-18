N, A, B = list(map(int, input().split()))

x = N // (A + B)
y = N % (A + B)

print((A * x + A if y >= A else A * x + y))
