import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N, M = list(map(int, readline().split()))
    A = list([int(x) - 1 for x in readline().split()])

    b = [0] * M

    for i in range(N - 1):
        prev = A[i]
        cur = A[i + 1]
        if prev < cur:
            b[prev + 1] += 1
            b[cur] -= 1
        else:
            if (prev + 1) % M > 0:
                b[(prev + 1) % M] += 1
            b[0] += 1
            b[cur] -= 1

    acc = [0] * M

    for i in range(M):
        if i > 0:
            acc[i] = acc[i - 1] + b[i]
        else:
            acc[i] = b[i]

    score = 0

    cnt = [0] * M

    for i in range(N - 1):
        prev = A[i]
        cur = A[i + 1]
        cnt[cur] += (cur + M - prev - 1) % M

    for i in range(N - 1):
        prev = A[i]
        cur = A[i + 1]
        first = (cur + M - prev) % M
        second = (cur + M) % M + 1
        score += min(first, second)
    ans = score

    for i in range(1, M):
        score += cnt[i - 1]
        score -= acc[i - 1]
        ans = min(ans, score)

    print(ans)


def __starting_point():
    main()


__starting_point()
