# coding: utf-8


def main():
    A, B = list(map(int, input().split()))
    ans = -1
    for i in range(10001):
        if i * 8 // 100 == A and i // 10 == B:
            ans = i
            break

    print(ans)


def __starting_point():
    main()


__starting_point()
