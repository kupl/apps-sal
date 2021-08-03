def solve():
    from sys import stdin
    f_i = stdin

    H, W = map(int, f_i.readline().split())
    A = tuple(tuple(map(int, f_i.readline().split())) for i in range(H))
    B = tuple(tuple(map(int, f_i.readline().split())) for i in range(H))

    dp1 = [0] * W
    bit_width = 80 * (H + W - 2)
    dp1[0] = 1 << (bit_width)
    for A_i, B_i in zip(A, B):
        dp2 = [0] * W

        diff = abs(A_i[0] - B_i[0])
        dp2[0] = (dp1[0] << diff) | (dp1[0] >> diff)

        for j, t in enumerate(zip(A_i[1:], B_i[1:]), start=1):
            A_ij, B_ij = t
            diff = abs(A_ij - B_ij)
            b = dp1[j] | dp2[j - 1]
            dp2[j] = (b << diff) | (b >> diff)

        dp1 = dp2

    b = bin(dp2[-1])
    b = b[-bit_width - 1:]
    print(b.index('1'))


solve()
