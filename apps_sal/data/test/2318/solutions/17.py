import sys


def check_str(s, t):
    i, j = 0, 0
    ls, lt = len(s), len(t)
    while i < ls:
        cur, cnt = s[i], 0
        while i < ls and s[i] == cur:
            cnt += 1
            i += 1

        while j < lt and t[j] == cur:
            cnt -= 1
            j += 1

        if cnt > 0:
            return False

    return True if j == lt else False


def main():
    n = int(input())
    for _ in range(n):
        s = input()
        t = input()
        print('YES' if check_str(s, t) else 'NO')


def __starting_point():
    if len(sys.argv) > 1 and sys.argv[1] == 'True':
        IS_LOCAL = True
    main()

__starting_point()
