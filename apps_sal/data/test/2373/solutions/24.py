
url = "https://atcoder.jp//contests/abc072/tasks/arc082_b"


def main():
    n = input()
    p = list(map(int, input().split()))
    count = 0
    for i, v in enumerate(p):
        if i == len(p) - 1 and i + 1 == v:
            count += 1
            break
        if i + 1 == v:
            p[i] = p[i + 1]
            p[i + 1] = v
            count += 1
    print(count)


def __starting_point():
    main()


__starting_point()
