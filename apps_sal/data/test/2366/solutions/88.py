from collections import defaultdict


def main():
    n = int(input())
    a = list(map(int, input().split(" ")))
    d = defaultdict(lambda: 0)
    d2 = {}
    for i in a:
        d[i] += 1
    for i, j in d.items():
        x = j * (j - 1) // 2
        d2[i] = x
    ans = 0
    ans = sum(d2.values())
    for i in range(n):
        print(ans - d[a[i]] + 1)


def __starting_point():
    main()


__starting_point()
