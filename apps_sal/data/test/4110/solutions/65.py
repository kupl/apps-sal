import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    (D, G, *PC) = list(map(int, read().split()))
    P = PC[::2]
    C = PC[1::2]
    ans = INF
    for mask in range(1 << D):
        problems = score = 0
        for i in range(D):
            if mask & 1 << i:
                problems += P[i]
                score += 100 * (i + 1) * P[i] + C[i]
            else:
                idx_max = i
        if score >= G:
            if ans > problems:
                ans = problems
            continue
        if score + 100 * (idx_max + 1) * (P[idx_max] - 1) >= G:
            problems += (G - score + 100 * (idx_max + 1) - 1) // (100 * (idx_max + 1))
            if ans > problems:
                ans = problems
    print(ans)
    return


def __starting_point():
    main()


__starting_point()
