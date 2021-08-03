T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    if N % 2:
        X = [i if i < N // 2 else N - i - 1 for i in range(N)]
        if all(a >= x for a, x in zip(A, X)):
            print('Yes')
        else:
            print('No')
    else:
        X = [i if i < N // 2 + 1 else N - i - 1 for i in range(N)]
        if all(a >= x for a, x in zip(A, X)):
            print('Yes')
            continue
        X[N // 2 - 1], X[N // 2] = X[N // 2], X[N // 2 - 1]
        if all(a >= x for a, x in zip(A, X)):
            print('Yes')
        else:
            print('No')
