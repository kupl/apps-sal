#!/usr/bin/env python3

# input = stdin.readline

def solve(n, m, a, queries):
    res = 0
    cnt = 0
    queries += [[1, x] for x in a]
    queries = list(sorted(queries, key=lambda x: x[1], reverse=True))
    for query in queries:
        if cnt >= n:
            break
        else:
            res += query[1] * min(query[0], n - cnt)
            cnt += query[0]
    return res


def main():
    N, M = list(map(int, input().split()))
    a = list(map(int, input().split()))
    queries = list(list(map(int, input().split())) for _ in range(M))
    print((solve(N, M, a, queries)))


def __starting_point():
    main()


__starting_point()
