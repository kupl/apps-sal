import sys


def main():
    n, m = list(map(int, sys.stdin.readline().split()))

    s = sys.stdin.readline().rstrip()
    t = sys.stdin.readline().rstrip()

    r = 10000
    res = []
    for i in range(m - n + 1):
        p = []
        c = 0
        for j in range(n):
            if s[j] != t[i + j]:
                c += 1
                p.append(j + 1)
        if c < r:
            r = c
            res = p
    print(r)
    if r != 0:
        print(" ".join(map(str, res)))


main()
