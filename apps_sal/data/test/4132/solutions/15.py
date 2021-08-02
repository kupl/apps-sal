def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    before = A
    after = []
    for _ in range(pow(10, 9)):
        x = before[0]
        if len(before) == 1:
            print(x)
            return
        after.append(x)
        for i in range(1, len(before)):
            y = before[i] % x
            if y != 0:
                after.append(y)
        after.sort()
        before = after
        after = []


def __starting_point():
    main()


__starting_point()
