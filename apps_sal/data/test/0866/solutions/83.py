import math


def main():
    X, Y = [int(n) for n in input().split(" ")]
    if (X + Y) % 3 != 0 or Y > 2 * X or X > 2 * Y:
        print(0)
        return 0
    p = 1000000007
    n_move = int((X + Y) / 3)
    i_move = int((2 * X - Y) / 3)
    j_move = int((2 * Y - X) / 3)
    f = [1, 1]
    finv = [1, 1] + [0] * n_move
    for i in range(n_move):
        f.append((f[-1] * (i + 2)) % p)
    lf = len(f)
    finv[lf - 1] = modpower(f[-1], p - 2, p)
    for i in range(lf - 1):
        finv[lf - i - 2] = ((finv[lf - i - 1]) * (lf - i - 1)) % p
    print((f[n_move] * (finv[i_move] * finv[j_move]) % p) % p)


def modpower(a, p, d):
    pp = [a]
    for i in range(int(math.log2(p)) + 1):
        pp.append((pp[-1] ** 2) % d)
    b_p = format(p, 'b')
    m = 1
    for i in range(len(b_p)):
        if b_p[-i - 1] == "1":
            m = (m * pp[i]) % d
    return m


main()
