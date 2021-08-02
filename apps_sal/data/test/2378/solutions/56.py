import sys
sys.setrecursionlimit(2 * 10**5)
input = sys.stdin.readline


def calc_counts(n, edges):
    counts = [0] * n
    seen = [False] * n
    dfs(0, edges, seen, counts)
    return counts


def dfs(node, edges, seen, counts):
    count = 1
    seen[node] = True
    for to in edges[node]:
        if seen[to]:
            continue
        count += dfs(to, edges, seen, counts)
    counts[node] = count
    return count


def calc_blank(node, counts: list, edges, all, mod=10**9 + 7):
    n = len(counts)
    paths = edges[node]
    if len(paths) <= 1:
        return 0
    base = counts[node]
    result = all - 1
    for v in paths:
        count = counts[v]
        if count > base:
            count = n - base
        result -= pow(2, count, mod) - 1
        result %= mod

    return result


def main():
    mod = 10**9 + 7
    n = int(input())
    edges = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = list(map(int, input().split()))
        edges[a - 1].append(b - 1)
        edges[b - 1].append(a - 1)

    counts = calc_counts(n, edges)
    all = pow(2, n - 1, mod)
    blanks = 0
    for node in range(n):
        blank = calc_blank(node, counts, edges, all)
        blanks += blank
        blanks %= mod

    inv_denominator = pow(pow(2, n, mod), mod - 2, mod)
    ans = blanks * inv_denominator % mod
    print(ans)


def __starting_point():
    main()


__starting_point()
