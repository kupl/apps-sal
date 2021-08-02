from collections import Counter
url = "https://atcoder.jp//contests/abc058/tasks/arc071_a"


def main():
    s = [input() for _ in range(int(input()))]
    isall = Counter(s[0])
    for k in isall:
        for row in s:
            c_count = row.count(k)
            if c_count < isall[k]:
                isall[k] = c_count
    isall = sorted(isall.items())
    for k, v in isall:
        print(k * v, end="")


def __starting_point():
    main()


__starting_point()
