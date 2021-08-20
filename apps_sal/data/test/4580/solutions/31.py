from sys import stdin, stdout


def get_level(n):
    return min(n // 400, 8)


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    level_num = dict()
    for i in range(9):
        level_num[i] = 0
    for contestant in a:
        lvl = get_level(contestant)
        level_num[lvl] += 1
    min_num = 0
    for lvl in level_num:
        if level_num[lvl] > 0 and lvl < 8:
            min_num += 1
    max_num = min_num + level_num[8]
    if min_num < 1:
        min_num = 1
    print(min_num, max_num)


def main():
    solve()


def __starting_point():
    main()


__starting_point()
