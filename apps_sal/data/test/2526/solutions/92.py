def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()

    x, y, a, b, c = map(int, input().split())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    r = list(map(int, input().split()))
    p.sort(reverse=True)
    q.sort(reverse=True)
    r = p[:x] + q[:y] + r
    r.sort(reverse=True)
    print(sum(r[:x + y]))


def __starting_point():
    main()


__starting_point()
