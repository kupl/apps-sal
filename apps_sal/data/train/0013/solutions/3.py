def iinput():
    return [int(x) for x in input().split()]


def main():
    n, g, b = iinput()
    z = (n + 1) // 2
    d = (z - 1) // g
    return max(d * b + z, n)


for i in range(int(input())):
    print(main())

