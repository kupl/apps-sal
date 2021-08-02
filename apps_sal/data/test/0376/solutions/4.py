import sys


def solve():
    n = int(sys.stdin.readline().rstrip())
    a = [int(i) for i in sys.stdin.readline().split()]
    Adj = [[] for i in range(n)]

    for i in range(n - 1):
        u, v = map(int, sys.stdin.readline().split())
        u, v = u - 1, v - 1
        Adj[u].append(v)
        Adj[v].append(u)

    max_v = max(a)
    num_m = sum(ai == max_v for ai in a)

    if num_m == 1:
        ans = max_v
        max_n = a.index(max_v)

        rinsetu = set(Adj[max_n])
        rinsetu.add(max_n)

        for u in range(n):
            if u in rinsetu:
                continue
            if a[u] == max_v - 1:
                ans = max_v + 1
                break
    else:
        for u in range(n):
            cnt = 0

            if a[u] == max_v:
                cnt += 1

            for v in Adj[u]:
                if a[v] == max_v:
                    cnt += 1

            if cnt == num_m:
                ans = max_v + 1
                break
        else:
            ans = max_v + 2

    print(ans)


def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None


def __starting_point():
    solve()


__starting_point()
