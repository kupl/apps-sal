n = int(input())

X = list(map(int, input().split()))

_min = min(X)

_max = max(X)

if _max < _min + 2:

    print(n)

    print(*X)

else:

    A = X.count(_min)

    B = X.count(_min + 1)

    C = X.count(_min + 2)

    best = n

    best_D = -1

    for D in range(- (B // 2), min(A, C) + 1):

        curr = min(A - D, A) + min(B, B + 2 * D) + min(C, C - D)

        if curr < best:

            best_D = D
            best = curr

    print(best)

    print(*([_min for _ in range(A - best_D)] + [_min + 1 for _ in range(B + 2 * best_D)] + [_min + 2 for _ in range(C - best_D)]))
