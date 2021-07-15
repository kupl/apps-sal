def solve(a):
    s = sum(a)
    if s % 2 == 1:
        return False
    s //= 2

    elements = set()
    cs = 0
    n = len(a)

    for i in range(n):
        cs += a[i]
        if cs == s:
            return True

        elements.add(a[i])

        if i > 0 and cs > s and cs - s in elements:
            return True

    return False


def main():
    n = int(input())
    a = list(map(int, input().split()))

    if solve(a):
        print("YES")
    elif solve(a[::-1]):
        print("YES")
    else:
        print("NO")


def __starting_point():
    # import sys
    # sys.stdin = open("in.txt")
    main()

__starting_point()
