(N, A, B) = map(int, input().split())
if N % (A + B) <= A:
    print(A * (N // (A + B)) + N % (A + B))
else:
    print(A * (N // (A + B)) + A)
