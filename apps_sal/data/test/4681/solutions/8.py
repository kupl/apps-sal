N = int(input())

if N == 0:
    print(2)
elif N == 1:
    print(1)
else:

    n_2 = 2
    n_1 = 1

    for _ in range(N - 1):
        n_0 = n_1 + n_2
        n_2 = n_1
        n_1 = n_0

    print(n_0)
