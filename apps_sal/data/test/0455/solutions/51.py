def solve(x, y, d, m):
    ret = ''
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    mode = ['R', 'U', 'D', 'L']
    for i in range(m):
        dir = 0
        t = abs(x + d[i] * dx[0]) + abs(y + d[i] * dy[0])
        for j in range(4):
            nx = x + d[i] * dx[j]
            ny = y + d[i] * dy[j]
            if abs(nx) + abs(ny) < t:
                t = abs(nx) + abs(ny)
                dir = j
        x = x + d[i] * dx[dir]
        y = y + d[i] * dy[dir]
        ret += mode[dir]
    print(ret)


def main():
    m = 34
    (X, Y, d) = ([], [], [])
    for i in range(32, 0, -1):
        d += [2 ** i]
    d += [1]
    N = int(input())
    (even, odd) = (0, 0)
    for i in range(N):
        (x, y) = map(int, input().split())
        X += [x]
        Y += [y]
        if (abs(x) + abs(y)) % 2 == 0:
            even += 1
        else:
            odd += 1
    if even and odd:
        print(-1)
        return 0
    if odd:
        m -= 1
    else:
        d += [1]
    print(m)
    print(' '.join(map(str, d)))
    for i in range(N):
        solve(X[i], Y[i], d, m)


main()
