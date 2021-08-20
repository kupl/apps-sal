import sys


def main():
    g = list(sys.stdin.readline().rstrip())
    s = list(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline())
    star = -1
    for i in range(len(s)):
        if s[i] == '*':
            star = i
    for i in range(n):
        t = sys.stdin.readline().rstrip()
        ok = True
        if star == -1 and len(s) > len(t) or (star != -1 and len(s) - 1 > len(t)):
            print('NO')
            continue
        for j in range(star):
            if s[j] == '?':
                if t[j] not in g:
                    ok = False
                    break
            elif t[j] != s[j]:
                ok = False
                break
        if not ok:
            print('NO')
            continue
        if len(t) < len(s) - star - 1:
            print('NO')
            continue
        for j in range(len(s) - star - 1):
            k = len(t) - j - 1
            m = len(s) - j - 1
            if s[m] == '?':
                if t[k] not in g:
                    ok = False
                    break
            elif t[k] != s[m]:
                ok = False
                break
        if not ok:
            print('NO')
            continue
        if star == -1 and len(s) == len(t):
            print('YES')
            continue
        if star == -1:
            print('NO')
            continue
        for j in range(star, len(t) - (len(s) - star - 1)):
            if t[j] in g:
                ok = False
                break
        if not ok:
            print('NO')
            continue
        print('YES')


main()
