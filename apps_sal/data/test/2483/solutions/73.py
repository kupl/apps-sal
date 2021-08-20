def main():
    import sys
    input = sys.stdin.readline
    from heapq import heappush
    (N, C) = map(int, input().split())
    table = [[0] * 10 ** 5 for _ in range(C)]
    for _ in range(N):
        (s, t, c) = map(int, input().split())
        s -= 1
        t -= 1
        c -= 1
        for i in range(s, t + 1):
            table[c][i] = 1
    ans = 0
    for i in range(10 ** 5):
        tmp = sum((table[j][i] for j in range(C)))
        ans = max(ans, tmp)
    print(ans)


def __starting_point():
    main()


__starting_point()
