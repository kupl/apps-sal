import sys
input = sys.stdin.readline


def main():
    n = int(input())

    if n == 1:
        print((1))
        return

    left = 1
    right = (n + 1)
    result = 0
    while(True):
        k = (right + left) // 2
        if k == right or k == left:
            break

        temp = k * (k + 1) // 2
        if temp <= n + 1:
            left = k
            result = k
        else:
            right = k

    print((n - result + 1))


def __starting_point():
    main()


__starting_point()
