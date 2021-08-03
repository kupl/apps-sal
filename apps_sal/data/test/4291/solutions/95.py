import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, Q = list(map(int, readline().split()))
    S = readline().strip()
    (*LR,) = list(map(int, read().split()))

    vec = [0] * (N + 1)
    for i in range(N - 1):
        vec[i + 1] = vec[i]
        if S[i] == 'A' and S[i + 1] == 'C':
            vec[i + 1] += 1

    ans = [0] * Q
    for i, (l, r) in enumerate(zip(*[iter(LR)] * 2)):
        l -= 1
        r -= 1
        ans[i] = vec[r] - vec[l]

    print(('\n'.join(map(str, ans))))
    return


def __starting_point():
    main()


__starting_point()
