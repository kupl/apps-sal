import sys

s = sys.stdin.readline().rstrip()
n = len(s)


def main():
    m = n // 2
    if n & 1:
        l = s[m::-1]
        r = s[m:]
    else:
        l = s[m - 1::-1]
        r = s[m:]
    base = l[0]

    cnt = m
    i = 0
    if n & 1:
        m += 1
    while i < m:
        if l[i] == r[i] == base:
            i += 1
            cnt += 1
        else:
            break
    return cnt


def __starting_point():
    ans = main()
    print(ans)


__starting_point()
