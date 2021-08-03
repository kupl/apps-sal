
url = "https://atcoder.jp//contests/abc129/tasks/abc129_a"


def main():
    p, q, r = list(map(int, input().split()))
    print((sum([p, q, r]) - max(p, q, r)))


def __starting_point():
    main()


__starting_point()
