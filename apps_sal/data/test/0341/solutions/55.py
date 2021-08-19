import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    (N, K) = list(map(int, readline().split()))
    point = list(map(int, readline().split()))
    T = readline().strip()
    T = list(map(int, T.translate(str.maketrans('rsp', '012'))))
    hand = [0] * N
    ans = 0
    for (i, h) in enumerate(T):
        win = (h - 1) % 3
        if i >= K and win == hand[i - K]:
            hand[i] = -1
        else:
            hand[i] = win
            ans += point[win]
    print(ans)
    return


def __starting_point():
    main()


__starting_point()
