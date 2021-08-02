
url = "https://atcoder.jp//contests/abc110/tasks/abc110_b"


def main():
    n, m, x, y = list(map(int, input().split()))
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))
    xs.sort()
    ys.sort()
    if xs[-1] >= ys[0]:
        print('War')
        return
    for i in range(xs[-1] + 1, ys[0] + 1):
        if x < i <= y:
            print('No War')
            return
    print('War')


def __starting_point():
    main()


__starting_point()
