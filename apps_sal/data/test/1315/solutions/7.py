def main():
    n = int(input())
    a = [int(x) for x in input().split(' ')]
    for i in range(len(a)):
        a[i] += i
    a.sort()
    for i in range(1, len(a)):
        a[i] -= i
        if a[i] < a[i - 1]:
            print(':(')
            return
    for i in range(len(a)):
        a[i] = str(a[i])
    print(' '.join(a))


def __starting_point():
    main()


__starting_point()
