(D, N) = list(map(int, input().split()))
if D == 0:
    if N == 100:
        print(101)
    else:
        print(N)
if D == 1:
    if N == 100:
        print(101 * 100)
    else:
        print(N * 100)
if D == 2:
    if N == 100:
        print(101 * 100 ** 2)
    else:
        print(N * 100 ** 2)
