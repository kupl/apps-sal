import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N, D, A = list(map(int, input().split()))
    monster = {}
    X = []
    for _ in range(N):
        x, h = list(map(int, input().split()))
        monster[x] = h
        X.append(x)

    X.sort()

    # x, damage
    q = deque([])

    acc_damage = 0

    ans = 0
    for i in range(N):
        x = X[i]
        h = monster[x]

        while q and q[0][0] < x:
            p, damage = q.popleft()
            acc_damage -= damage

        if h - acc_damage <= 0:
            continue

        cnt = (h - acc_damage + A - 1) // A
        ans += cnt
        acc_damage += cnt * A

        q.append((x + 2 * D, cnt * A))

    print(ans)


def __starting_point():
    main()


__starting_point()
