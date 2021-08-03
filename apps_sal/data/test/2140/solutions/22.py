def main():
    s = input()
    s = [s[i] for i in range(len(s))]
    m = int(input())
    a = [int(x) for x in input().split()]
    b = [0 for i in range(int(len(s) / 2 + 1))]
    for i in range(m):
        b[a[i] - 1] += 1
    for i in range(0, int(len(s) / 2)):
        if i > 0:
            b[i] += b[i - 1]
        if b[i] % 2 == 1:
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
    return "".join(s)


def __starting_point():
    print(main())


__starting_point()
