D, N = list(map(int, input().split()))
if D == 0:
    if N <= 99:
        print(N)
    else:
        print((N + 1))
if D == 1:
    if N <= 99:
        print((N * 100))
    else:
        print((N * 100 + 100))
if D == 2:
    if N <= 99:
        print((N * 10000))
    else:
        print((N * 10000 + 10000))
