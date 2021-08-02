
url = "https://atcoder.jp//contests/abc070/tasks/abc070_b"


def main():
    t = list(map(int, input().split()))
    start = max(t[0], t[2])
    end = min(t[1], t[3])
    if end >= start:
        print((end - start))
    else:
        print((0))


def __starting_point():
    main()


__starting_point()
