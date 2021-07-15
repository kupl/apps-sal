def main():
    from collections import Counter
    n, cnt = int(input()), Counter()
    l = sorted((tuple(map(int, input().split())) for _ in range(n)), reverse=True)
    for i in range(1, n):
        x, y = l[i]
        for j in range(i):
            u, v = l[j]
            cnt[u - x, v - y] += 1
    print(sum(i * (i - 1) for i in list(cnt.values())) // 4)


def __starting_point():
    main()

__starting_point()
