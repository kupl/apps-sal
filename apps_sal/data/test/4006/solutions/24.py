import sys


def main():
    num = int(input())
    seen = set()
    while num:
        if num in seen:
            break
        seen.add(num)
        num += 1
        while num % 10 == 0:
            num //= 10
    print(len(seen))


def __starting_point():
    main()


__starting_point()
