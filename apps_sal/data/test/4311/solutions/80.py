url = 'https://atcoder.jp//contests/abc116/tasks/abc116_b'


def calc(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


def main():
    s = int(input())
    ans = [s]
    while True:
        tmp = calc(ans[-1])
        ans.append(tmp)
        if ans.index(tmp) != len(ans) - 1:
            print(len(ans))
            break


def __starting_point():
    main()


__starting_point()
