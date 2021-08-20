from collections import defaultdict


def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(lambda: 0)
    ans = 0
    for (i, ai) in enumerate(a, 1):
        num = str(ai + i)
        d[num] += 1
        ans += d[str(i - ai)]
    print(ans)


def __starting_point():
    main()


__starting_point()
