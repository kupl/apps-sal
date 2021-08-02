import sys


def main():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().rstrip()

    r = ['a'] * n
    if n % 2 == 1:
        p = n // 2
        r[p] = s[0]
        j = 1
        for i in range(1, n, 2):
            r[p - j] = s[i]
            r[p + j] = s[i + 1]
            j += 1

    else:
        p = n // 2 - 1
        j = 1
        for i in range(0, n, 2):
            r[p - j + 1] = s[i]
            r[p + j] = s[i + 1]
            j += 1

    print(''.join(r))


main()
