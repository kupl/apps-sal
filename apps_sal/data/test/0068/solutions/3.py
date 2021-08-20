def valid(step, tx, ty, nx, ny, s, d):
    fx = 0
    fy = 0
    for i in range(len(s)):
        c = s[i]
        fx += d[c][0]
        fy += d[c][1]
        if i >= step:
            c = s[i - step]
            fx -= d[c][0]
            fy -= d[c][1]
        if i >= step - 1:
            diff = abs(nx - fx - tx) + abs(ny - fy - ty)
            if diff <= step and (step - diff) % 2 == 0:
                return True
    return False


def main():
    d = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    nx = 0
    ny = 0
    n = int(input())
    s = input()
    (tx, ty) = [int(x) for x in input().split(' ')]
    diff = abs(tx) + abs(ty)
    if diff > len(s) or (diff - len(s)) % 2 == 1:
        print(-1)
        return
    for c in s:
        nx += d[c][0]
        ny += d[c][1]
    if (nx, ny) == (tx, ty):
        print(0)
        return
    l = 0
    r = len(s)
    ans = r
    while l < r:
        m = (l + r) // 2
        if valid(m, tx, ty, nx, ny, s, d):
            ans = m
            r = m
        else:
            l = m + 1
    print(ans)


def __starting_point():
    main()


__starting_point()
