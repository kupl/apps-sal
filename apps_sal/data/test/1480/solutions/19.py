import sys

def solve():
    n, k = map(int, input().split())
    ch = [i + 1 for i in range(n)]
    a = [int(i) for i in input().split()]

    live = n
    leader = 0
    ans = []

    for v in a:
        v = v % live
        j = 0
        cnt = 0

        while cnt < v:
            if ch[(leader + j + 1) % n]:
                cnt += 1

            j += 1

        ans.append((leader + j) % n + 1)
        ch[(leader + j) % n] = 0
        live -= 1
        leader = (leader + j + 1) % n

        while ch[leader] == 0:
            leader = (leader + 1) % n

        # print(ch)
        # print(leader + 1)

    print(*ans)

def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None

def __starting_point():
    solve()
__starting_point()
