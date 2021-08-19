import sys
read = sys.stdin.read
readlines = sys.stdin.readlines


def main():
    n = int(input())
    s = input()
    res = s.count('R') * s.count('G') * s.count('B')
    if res == 0:
        print(0)
        return
    for i1 in range(n):
        for i2 in range(i1 + 1, n):
            if i2 * 2 - i1 <= n - 1:
                if s[i1] != s[i2]:
                    res -= s[i1] != s[i2 * 2 - i1] and s[i2] != s[i2 * 2 - i1]
    print(res)


def __starting_point():
    main()


__starting_point()
