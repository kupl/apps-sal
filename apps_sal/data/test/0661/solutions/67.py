#!python3

def LI():
    return list(map(int, input().split()))


# input
M, K = LI()


def solve():
    n = 2 ** M
    l = [i for i in range(n) if i != K]
    ret = l + [K] + l[::-1] + [K]
    return ret


def main():
    if K >= 2 ** M:
        ans = [-1]
    elif M == 1:
        if K == 0:
            ans = [0, 0, 1, 1]
        else:
            ans = [-1]
    else:
        ans = solve()

    print((*ans))


def __starting_point():
    main()


__starting_point()
