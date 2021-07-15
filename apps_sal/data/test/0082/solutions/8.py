import sys

def solve():
    n, k = map(int, input().split())
    a = [int(i) for i in input().split()]

    tot = sum(a)
    cnt = 0

    while int(tot / n + 0.5) < k:
        tot += k
        n += 1
        cnt += 1

    print(cnt)

def __starting_point():
    solve()
__starting_point()
