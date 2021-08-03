import math


def main():
    n = int(input())
    cnt = 0
    for a in range(1, n):
        for b in range(1, n):
            if n - a * b > 0:
                cnt += 1
            else:
                break
    print(cnt)


def __starting_point():
    main()


__starting_point()
