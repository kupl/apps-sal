import sys
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    n, m = map(int, input().split())
    l = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in [-1, 1]:
        for j in [-1, 1]:
            for k in [-1, 1]:
                l2 = []
                for (x, y, z) in l:
                    s = x * i + y * j + z * k
                    l2.append(s)
                l2 = sorted(l2, reverse=True)
                ans = max(ans, sum(l2[:m]))
    print(ans)


def __starting_point():
    main()

__starting_point()
