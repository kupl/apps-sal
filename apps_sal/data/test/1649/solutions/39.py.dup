def main():
    a = list(map(int, input().split()))

    # 1
    for v in a:
        if v == sum(a) - v:
            print("Yes")
            return

    # 2
    for i in range(4):
        for j in range(4):
            if i == j:
                continue
            if a[i] + a[j] == sum(a) - (a[i] + a[j]):
                print("Yes")
                return

    print("No")


def __starting_point():
    main()


__starting_point()
