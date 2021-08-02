
url = "https://atcoder.jp//contests/abc107/tasks/arc101_a"


def main():
    n, k = list(map(int, input().split()))
    xs = list(map(int, input().split()))
    ans = 100000000000000
    se = [0, k - 1]
    while se[1] < n:
        if xs[se[0]] < 0 <= xs[se[1]]:
            tmp = min(abs(xs[se[0]]), xs[se[1]]) * 2 + max(abs(xs[se[0]]), xs[se[1]])
            ans = min(ans, tmp)
        elif xs[se[0]] < 0:
            ans = min(ans, abs(xs[se[0]]))
        elif xs[se[1]] >= 0:
            ans = min(ans, xs[se[1]])
        se = [v + 1 for v in se]
    print(ans)


def __starting_point():
    main()


__starting_point()
