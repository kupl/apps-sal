import sys
inf = 1 << 30


def solve():
    n = int(input())
    a = [inf if ai != '0' else 0 for ai in input().split()]
    for i in range(n):
        if a[i] == 0:
            for j in range(i - 1, -1, -1):
                if a[j] > i - j:
                    a[j] = i - j
                else:
                    break
            for j in range(i + 1, n):
                if a[j] > j - i:
                    a[j] = j - i
                else:
                    break
    print(*a)


def __starting_point():
    solve()


__starting_point()
