import sys
input = sys.stdin.readline


def main():
    s = input().strip()[::-1]
    while True:
        ok = False
        if len(s) >= 7:
            if s[:7] == 'remaerd':
                s = s[7:]
                ok = True
        if len(s) >= 6:
            if s[:6] == 'resare':
                s = s[6:]
                ok = True
        if len(s) >= 5:
            if s[:5] == 'esare' or s[:5] == 'maerd':
                s = s[5:]
                ok = True
        if not ok:
            break
    if len(s) > 0:
        print('NO')
    else:
        print('YES')


def __starting_point():
    main()


__starting_point()
