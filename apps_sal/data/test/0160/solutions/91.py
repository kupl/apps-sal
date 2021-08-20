import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def divisors(n):
    lower = []
    upper = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            lower.append(i)
            if i != n // i:
                upper.append(n // i)
    lower.extend(reversed(upper))
    return lower


def main():
    (N, K, *A) = list(map(int, read().split()))
    total = sum(A)
    div = divisors(total)
    for d in reversed(div):
        vec = [a % d for a in A if a % d]
        if not vec:
            print(d)
            return
        vec.sort()
        M = len(vec)
        csum_sub = [0] * (M + 1)
        csum_add = [0] * (M + 1)
        for i in range(M):
            csum_sub[i + 1] = csum_sub[i] + vec[i]
            csum_add[i + 1] = csum_add[i] + d - vec[i]
        for i in range(1, M):
            if csum_sub[i] <= K and csum_sub[i] == csum_add[M] - csum_add[i]:
                print(d)
                return
    return


def __starting_point():
    main()


__starting_point()
