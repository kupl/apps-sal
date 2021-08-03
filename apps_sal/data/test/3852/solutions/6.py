N = int(input())
A = list(map(int, input().split()))
maxA = max(A)
minA = min(A)

if minA >= 0 or 2 * abs(maxA) > abs(minA):
    maxi = A.index(maxA)
    print((2 * N - 1))
    print((maxi + 1, maxi + 1))

    for i in range(N):
        if i == maxi:
            continue
        print((maxi + 1, i + 1))

    for i in range(N - 1):
        print((i + 1, i + 2))

else:
    mini = A.index(minA)
    print((2 * N - 1))
    print((mini + 1, mini + 1))
    for i in range(N):
        if i == mini:
            continue
        print((mini + 1, i + 1))

    for i in range(N - 1, 0, -1):
        print((i + 1, i))
