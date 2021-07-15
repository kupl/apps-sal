from collections import defaultdict


def solve():
    N = int(input())

    maxx = 0
    maxy = 0
    WS = defaultdict(list)

    for i in range(N):
        x, y = list(map(int, input().split()))
        WS[y - x].append((x, y))
        maxx = max(maxx, x)
        maxy = max(maxy, y)

    for w in WS:
        WS[w].sort(reverse=True)

    W = list(map(int, input().split()))

    ans = [None] * N

    mx = [0] * (maxy + 1)
    my = [0] * (maxx + 1)

    for i in range(N):
        w = W[i]
        if WS[w]:
            ans[i] = ax, ay = WS[w].pop()
            if mx[ay] == ax and my[ax] == ay:
                mx[ay] = ax + 1
                my[ax] = ay + 1

            else:
                print('NO')
                return
        else:
            print('NO')
            return

    print('YES')
    for a in ans:
        print(a[0], a[1])


def __starting_point():
    solve()

__starting_point()
