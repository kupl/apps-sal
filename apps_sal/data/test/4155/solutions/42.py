import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *H = list(map(int, read().split()))

    ans = 0
    while True:
        changed = changed2 = False
        for i in range(N):
            if H[i] > 0:
                H[i] -= 1
                changed = True
                changed2 = True
            else:
                if changed:
                    ans += 1
                    changed = False
        if changed:
            ans += 1
        if not changed2:
            break

    print(ans)
    return


def __starting_point():
    main()

__starting_point()
