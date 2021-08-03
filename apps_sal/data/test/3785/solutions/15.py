from collections import deque, namedtuple
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def main():
    n, m, limit = map(int, input().split())
    a, sx, sy, tot = [], 0, 0, 0
    for i in range(n):
        s, t = input(), []
        for j, c in enumerate(s):
            if c == '.':
                sx, sy = i, j
                tot += 1
                c = 'X'
            t.append(c)
        a.append(t[:])

    dq, done = deque([(sx, sy)]), 0
    while len(dq) > 0:
        now = dq.popleft()
        if done >= tot - limit:
            break
        if(a[now[0]][now[1]] == 'X'):
            done += 1
        else:
            continue
        a[now[0]][now[1]] = '.'
        for i in range(4):
            tx, ty = dx[i] + now[0], dy[i] + now[1]
            if 0 <= tx < n and 0 <= ty < m and a[tx][ty] == 'X':
                dq.append((tx, ty))
    for i in a:
        print("".join(i))


def __starting_point():
    main()


__starting_point()
