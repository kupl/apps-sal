def __starting_point():

    n = int(input())

    A = [2, 1]
    for i in range(2, n + 1):
        A.append(A[i - 2] + A[i - 1])
    print(A[n])


__starting_point()
