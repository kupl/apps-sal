#!/usr/bin/env python3


def convert(a, b):
    path = [b]
    while b != a:
        if b % 2 == 0 and b > 0:
            b //= 2
            path.append(b)
        elif b % 10 == 1:
            b //= 10
            path.append(b)
        else:
            return None
    return reversed(path)


def main():
    ans = convert(*list(map(int, input().split())))
    if ans is None:
        print("NO")
    else:
        print("YES")
        path = list(ans)
        print(len(path))
        print(*path)


def __starting_point():
    main()


__starting_point()
