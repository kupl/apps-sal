import sys
import itertools
input = sys.stdin.readline


def main():
    n = int(input())
    s = []
    A = []
    B = []
    for _ in range(n):
        (a, b) = list(map(int, input().split()))
        s.append([a, b])
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    s.sort()
    ansA = 1
    ansB = 1
    anss = 1
    for (key, val) in itertools.groupby(A):
        f = len(list(val))
        for i in range(1, f + 1):
            ansA *= i
            ansA %= 998244353
    for (key, val) in itertools.groupby(B):
        f = len(list(val))
        for i in range(1, f + 1):
            ansB *= i
            ansB %= 998244353
    for (key, val) in itertools.groupby(s):
        f = len(list(val))
        for i in range(1, f + 1):
            anss *= i
            anss %= 998244353
    flag = 1
    for i in range(n - 1):
        if s[i + 1][1] < s[i][1] or s[i + 1][0] < s[i][0]:
            flag = 0
            break
    if flag == 0:
        anss = 0
    ansn = 1
    for i in range(1, n + 1):
        ansn *= i
        ansn %= 998244353
    print((ansn - ansA - ansB + anss) % 998244353)


def __starting_point():
    main()


__starting_point()
