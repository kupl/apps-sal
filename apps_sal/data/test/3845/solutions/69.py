
A, B = list(map(int, input().split()))


def paint1(ans):
    a = 1
    for i in range(0, 49, 2):
        for j in range(0, 100, 2):
            if a == A:
                return
            ans[i][j] = "."
            a += 1


def paint2(ans):
    b = 1
    for i in range(51, 100, 2):
        for j in range(0, 100, 2):
            if b == B:
                return
            ans[i][j] = "
            b += 1


def main():
    ans = [["
    paint1(ans)
    paint2(ans)

    print((100, 100))
    for r in ans:
        print(("".join(r)))


def __starting_point():
    main()


__starting_point()
