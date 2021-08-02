import math


def main():
    (n, k) = tuple([int(x) for x in input().split()])
    s = input()

    if n == 1:
        opt = '0'
    else:
        opt = '1' + '0' * (n - 1)

    r = []
    left = k
    for i in range(n):
        if s[i] != opt[i] and left > 0:
            left -= 1
            r.append(opt[i])
        else:
            r.append(s[i])

    print(''.join(r))


def __starting_point():
    main()


__starting_point()
