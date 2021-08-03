def main():
    import sys
    input = sys.stdin.readline
    l = [[0, 0, 0]]
    r = [[0, 0, 0]]
    n, c = map(int, input().split())
    for i in range(n):
        x, v = map(int, input().split())
        r.append([x, v])
        l.append([c - x, v])
    r.sort()
    l.sort()
    for x in (l, r):
        now = 0
        for i in range(n):
            now += x[i + 1][1]
            x[i + 1].append(max(now - x[i + 1][0], x[i][2]))
            if x[i + 1][2] == x[i][2]:
                x[i + 1][0] = x[i][0]
    ans = 0
    for i in range(n + 1):
        a = l[i][0]
        b = r[n - i][0]
        ans = max(l[i][2] + r[n - i][2] - min(a, b), ans)
    print(ans)


def __starting_point():
    main()


__starting_point()
