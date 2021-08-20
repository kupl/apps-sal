S = input()
(X, Y) = list(map(int, input().split()))


def judge(l, m):
    s = sum(l)
    t = s - m if m > 0 else s + m
    if t < 0 or t % 2 == 1:
        return False
    t //= 2
    n = len(l)
    w = [[False] * (t + 1) for _ in range(n + 1)]
    w[0][0] = True
    for i in range(1, n + 1):
        for j in range(t + 1):
            if w[i - 1][j]:
                w[i][j] = True
                if j + l[i - 1] <= t:
                    w[i][j + l[i - 1]] = True
    return w[-1][-1]


def main():
    n = len(S)
    d = 0
    for s in S:
        if s == 'F':
            d += 1
        else:
            break
    (dx, dy) = ([], [])
    side = True
    i = d
    while i < n:
        while i < n and S[i] == 'T':
            side = not side
            i += 1
        c = 0
        while i < n and S[i] == 'F':
            c += 1
            i += 1
        if side:
            dx.append(c)
        else:
            dy.append(c)
    b1 = judge(dx, X - d)
    b2 = judge(dy, Y)
    ans = 'Yes' if b1 and b2 else 'No'
    print(ans)


def __starting_point():
    main()


__starting_point()
