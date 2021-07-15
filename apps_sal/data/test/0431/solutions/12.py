import sys

inf = float('inf')
ans = inf

def solve():
    nonlocal ans
    n, m = map(int, input().split())
    room = [[int(i) for i in input()] for j in range(n)]
    room.reverse()

    exits = [False] * n

    for i in range(n - 1, -1, -1):
        if any(room[i]):
            exits[i] = True

        if i - 1 >= 0:
            exits[i - 1] |= exits[i]

    # print(exits)

    if not exits[0]:
        ans = 0
    else:
        dfs(0, n, m, room, exits, 0, 0)

    print(ans)

def dfs(floor, n, m, room, exits, pos, move):
    nonlocal ans

    k = -1

    if pos == 0:
        for j in range(m + 1, -1, -1):
            if room[floor][j]:
                k = j
                break
        else:
            k = 0
    else:
        for j in range(0, m + 2):
            if room[floor][j]:
                k = j
                break
        else:
            k = m + 1

    move += abs(k - pos)

    if floor == n - 1 or not exits[floor + 1]:
        ans = min(ans, move)
        return
    else:
        dfs(floor + 1, n, m, room, exits, 0, move + k + 1)
        dfs(floor + 1, n, m, room, exits, m + 1, move + m + 1 - k + 1)

def __starting_point():
    solve()
__starting_point()
