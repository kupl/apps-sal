def main():
    from math import gcd
    input()
    s = set(map(int, input().split()))
    x = a = s.pop()
    for b in s:
        a = gcd(a, b)
        if a == 1:
            break
    s.add(x)
    print(a if a in s else -1)


def __starting_point():
    main()


__starting_point()
