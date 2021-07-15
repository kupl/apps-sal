def main():
    from collections import Counter
    n, cnt, l = int(input()), Counter(), []
    for x, y in sorted((tuple(map(int, input().split())) for _ in range(n)), reverse=True):
        for u, v in l:
            cnt[u - x, v - y] += 1
        l.append((x, y))
    print(sum(i * (i - 1) for i in list(cnt.values())) // 4)


def __starting_point():
    main()

__starting_point()
