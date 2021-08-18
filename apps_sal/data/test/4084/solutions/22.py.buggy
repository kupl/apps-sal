N, A, B = map(int, input().split())
answer = 0

if A == 0:
    print(0)
    return

C = A + B
D = N // C
F = N % C

if F >= A:
    print((D + 1) * A)
else:
    print(D * A + F)
