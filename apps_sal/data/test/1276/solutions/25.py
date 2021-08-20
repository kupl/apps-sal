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
            i3 = i2 * 2 - i1
            if i3 <= n - 1:
                res -= s[i1] != s[i2] and s[i1] != s[i3] and (s[i2] != s[i3])
    print(res)


def __starting_point():
    main()


__starting_point()
