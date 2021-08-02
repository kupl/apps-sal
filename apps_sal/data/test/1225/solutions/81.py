# coding: utf-8

def main():
    N = 0
    H = int(input())
    ans = 0

    while (True):
        H //= 2
        if H == 0:
            break
        N += 1

    for i in range(N + 1):
        ans += pow(2, i)

    print(ans)


def __starting_point():
    main()


__starting_point()
