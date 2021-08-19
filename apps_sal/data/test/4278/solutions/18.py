import itertools
url = 'https://atcoder.jp//contests/abc137/tasks/abc137_c'


def main():
    n = int(input())
    maps = {}
    count = 0
    for i in range(n):
        s = sorted(input())
        s = ''.join(s)
        maps.setdefault(s, 0)
        maps[s] += 1
    for k in maps:
        count += maps[k] * (maps[k] - 1) // 2
    print(count)


def __starting_point():
    main()


__starting_point()
