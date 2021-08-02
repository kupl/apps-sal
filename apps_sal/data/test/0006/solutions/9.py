T = int(input())
for _ in range(T):
    N, X = list(map(int, input().split()))
    A = -1
    B = -1
    for i in range(N):
        d, h = list(map(int, input().split()))
        A = max(A, d - h)
        B = max(B, d)

    if B >= X:
        print(1)
    elif A > 0:
        print((X - B + A - 1) // A + 1)
    else:
        print(-1)
