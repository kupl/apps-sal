def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()

    n = int(input())
    s = input()
    cnt = 0
    m = 0
    for i in range(n):
        if s[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        m = min(m, cnt)
    ans = '(' * (-m) + s + ')' * (cnt - m)
    print(ans)


def __starting_point():
    main()


__starting_point()
