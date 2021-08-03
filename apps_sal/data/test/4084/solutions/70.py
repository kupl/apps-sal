N, A, B = list(map(int, input().split()))

print(((N // (A + B)) * A + min(A, N % (A + B))))
