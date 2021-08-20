from math import ceil


def solve():
    (n, x, y, d) = [int(x) for x in input().split()]
    INF = 1000000000.0
    sol1 = abs(x - y) // d if (x - y) % d == 0 else INF
    sol2 = ceil((x - 1) / d) + ceil((y - 1) / d) if (y - 1) % d == 0 else INF
    sol3 = ceil((n - x) / d) + ceil((n - y) / d) if (n - y) % d == 0 else INF
    ans = min(sol1, sol2, sol3)
    ans = ans if ans != INF else -1
    print(ans)


nt = int(input())
for _ in range(nt):
    solve()
