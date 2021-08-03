# coding: utf-8


def main():
    N = int(input())
    ans = sum(list(map(int, input().split()))) - N
    print(ans)


def __starting_point():
    main()


__starting_point()
