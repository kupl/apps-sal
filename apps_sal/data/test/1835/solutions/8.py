import sys
from collections import Counter
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def getN():
    return int(input())


def getList():
    return list(map(int, input().split()))


def solve():
    n = getN()
    iso = False
    ise = False
    cnt1, cnt0 = 0, 0
    for _ in range(n):
        s = input().strip()
        if len(s) % 2 == 1:
            iso = 1
        else:
            ise = 1

        cnt = Counter(s)
        cnt1 += cnt["1"]
        cnt0 += cnt["0"]

    if not iso and cnt1 % 2 and cnt0 % 2:
        print(n - 1)
    else:
        print(n)


def main():
    t = getN()
    for times in range(t):
        solve()


def __starting_point():
    main()


__starting_point()
