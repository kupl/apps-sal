url = 'https://atcoder.jp//contests/abc113/tasks/abc113_b'


def main():
    input()
    (t, a) = list(map(int, input().split()))
    syuto = list(map(int, input().split()))
    tempture = []
    for s in syuto:
        tempture.append(abs(a - (t - s * 0.006)))
    print(tempture.index(min(tempture)) + 1)


def __starting_point():
    main()


__starting_point()
