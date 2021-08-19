import sys
read = sys.stdin.read
#readlines = sys.stdin.readlines


def main():
    n = int(input())
    rc = tuple(input())
    rc2 = [c == 'W' for c in rc]
    r1 = sum(rc2)  # 白をすべて赤にした場合
    r2 = n - r1  # 赤をすべて白にした場合。
    r3 = sum(rc2[:r2])  # 赤を左につめるのに邪魔になる白の数
    print((min(r1, r2, r3)))


def __starting_point():
    main()


__starting_point()
