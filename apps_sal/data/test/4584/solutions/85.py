def __starting_point():

    n = int(input())
    A = list(map(int, input().split()))

    B = [0] * n
    for a in A:
        B[a - 1] += 1
    for b in B:
        print(b)


__starting_point()
