import sys


def add_one(p):
    count = 0
    for i in range(len(p) - 1, -1, -1):
        if p[i] == '9':
            count += 1
        else:
            return p[: -1 - count] + str(int(p[i]) + 1) + '0' * count, 0
    return '0' * count, 1


def __starting_point():
    L = int(input())
    A = input()
    if len(A) % L == 0:
        p_size = int(len(A) / L)
        p = A[:L]
        for i in range(2, p_size + 1):
            num = A[(i - 1) * L: i * L]
            if p > num:
                print(A[:L] * p_size)
                return
            elif p < num:
                p, _ = add_one(p)
                print(p * p_size)
                return
        p, c = add_one(p)
        if c == 1:
            print(('1' + '0' * (L - 1)) * (p_size + 1))
        else:
            print(p * p_size)
    else:
        print(('1' + '0' * (L - 1)) * (int(len(A) / L) + 1))


__starting_point()
