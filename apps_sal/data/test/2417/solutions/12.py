import math


def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    out = set()
    j = 0
    result = 0
    for i in range(n):
        if b[i] != a[j]:
            out.add(b[i])
            result += 1
        else:
            j += 1
            while j < n and a[j] in out:
                j += 1
    print(result)


def __starting_point():
    main()


__starting_point()
