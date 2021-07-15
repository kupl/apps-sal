LI = lambda: list(map(int, input().split()))

N = int(input())
V = LI()
C = LI()


def main():
    ans = 0
    for v, c in zip(V, C):
        if v > c:
            ans += v - c
    print(ans)


def __starting_point():
    main()

__starting_point()
