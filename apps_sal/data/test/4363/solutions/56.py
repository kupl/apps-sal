import itertools
url = "https://atcoder.jp//contests/abc057/tasks/abc057_a"


def main():
    k, s = list(map(int, input().split()))
    count = 0
    for x, y in itertools.product(range(k + 1), range(k + 1)):
        z = s - x - y
        if 0 <= z <= k:
            count += 1
    print(count)


def __starting_point():
    main()


__starting_point()
