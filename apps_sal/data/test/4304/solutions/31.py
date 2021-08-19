def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(' '))


def main():
    (a, b) = Input()
    towers = [1] * 999
    for i in range(1, 999):
        towers[i] = towers[i - 1] + i + 1
    n = b - a
    ans = 0
    for i in range(998):
        if towers[i + 1] - towers[i] == n:
            ans = towers[i] - a
    print(ans)


main()
