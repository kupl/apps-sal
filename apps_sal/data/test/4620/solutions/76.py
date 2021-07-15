import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *CSF = map(int, read().split())
    train = [0] * (N - 1)
    for i, t in enumerate(zip(*[iter(CSF)] * 3)):
        train[i] = t

    ans = [0] * N
    for i in range(N - 1):
        t = 0
        for c, s, f in train[i:]:
            if t < s:
                t = s + c
            else:
                t += f - ((t - 1) % f + 1) + c
        ans[i] = t

    ans[N - 1] = 0
    print(*ans, sep='\n')
    return


def __starting_point():
    main()

__starting_point()
