N, M = [int(n) for n in input().split()]

if N == 1 and M == 1:
    print((1))
elif N == 2 and M == 1:
    print((0))
elif N == 1 and M == 2:
    print((0))
elif N == 2 and M == 2:
    print((0))
elif N == 1 and M > 2:
    print((M - 2))
elif N > 2 and M == 1:
    print((N - 2))
else:
    print(((N - 2) * (M - 2)))
