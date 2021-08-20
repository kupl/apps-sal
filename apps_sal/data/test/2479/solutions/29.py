import sys
input = sys.stdin.readline


def main():
    (n, q) = list(map(int, input().split()))
    ans = (n - 2) ** 2
    h = n
    w = n
    a = [n for _ in range(n)]
    b = [n for _ in range(n)]
    for _ in range(q):
        (t, x) = list(map(int, input().split()))
        if t == 1:
            if x < w:
                for i in range(x, w):
                    a[i] = h
                w = x
            ans -= a[x] - 2
        else:
            if x < h:
                for i in range(x, h):
                    b[i] = w
                h = x
            ans -= b[x] - 2
    print(ans)


def __starting_point():
    main()


__starting_point()
