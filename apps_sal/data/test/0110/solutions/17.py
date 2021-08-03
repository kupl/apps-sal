def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    for i in range(n):
        if a[i] >= 0:
            a[i] = -a[i] - 1
    amin = 0
    posmin = 0
    if n % 2 == 1:
        for i in range(n):
            if a[i] < amin:
                amin = a[i]
                posmin = i
        a[posmin] = -a[posmin] - 1
    for ai in a:
        print(ai, end=" ")


def __starting_point():
    main()


__starting_point()
