import sys

def solve():
    n, f = map(int, input().split())
    k = [0] * n
    l = [0] * n
    d = [0] * n

    for i in range(n):
        ki, li = map(int, sys.stdin.readline().split())
        k[i] = ki
        l[i] = li

        if 2*ki > li:
            d[i] = max(li - ki, 0)
        else:
            d[i] = ki

    d.sort(reverse=True)

    ans = sum(d[:f]) + sum(min(k[i], l[i]) for i in range(n))

    print(ans)



def __starting_point():
    solve()
__starting_point()
