N = int(input())


def base(x, n):
    ret = []
    while x != 0:
        ret.append(x % abs(n))
        if n < 0:
            x = -(-x // n)
        else:
            x //= n
    return ret


if N == 0:
    print(0)
else:
    print(''.join(map(str, reversed(base(N, -2)))))
