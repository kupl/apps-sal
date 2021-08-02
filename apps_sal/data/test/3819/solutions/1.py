if True:
    N = int(input())
    A = [int(a) for a in input().split()]
    B = [int(a) for a in input().split()]
else:
    A = [0, 0, 0, 5, 0, 0, 0, 4, 0, 0, 11]
    B = [9, 2, 6, 0, 8, 1, 7, 0, 3, 0, 10]
    A = [0, 2, 0]
    B = [3, 0, 1]
    N = len(A)


def chk():
    i = 0
    while B[i] != 1:
        i += 1
        if i == N:
            return 0
    j = i - 1
    # print("k =", j)
    while i < N:
        # print("i, B[i], N, k, i-N+k =", i, B[i], N, j, i-j)
        if B[i] != i - j:
            # print("DD")
            return 0
        i += 1
    # print("j =", j)
    for i in range(j + 1):
        # print(B[i], N+1-j+i)
        if 0 < B[i] < N + 1 - j + i:
            # print("EE")
            return 0
    # print(j+1)
    return j + 2


c = chk()
if c > 0:
    print(c - 1)
else:
    # print([max(i-B[i]+2, 0) for i in range(N)])
    print(max([max(i - B[i] + 2, 0) if B[i] else 0 for i in range(N)]) + N)
