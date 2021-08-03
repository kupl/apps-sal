def readinput():
    n = int(input())
    return n


def main(n):
    for k in range(n // 4 + 1):
        if (n - 4 * k) % 7 == 0:
            return 'Yes'
    else:
        return 'No'


def __starting_point():
    n = readinput()
    ans = main(n)
    print(ans)


__starting_point()
