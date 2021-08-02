def main():
    n = int(input())
    pt = []
    for _ in range(n):
        x, y = map(int, input().split())
        pt.append([x, y])
    a, b, c = [], [], []
    for p in pt:
        a.append(p[0] + p[1])
        b.append(p[0] - p[1])
        c.append(p[1] - p[0])
    ans = 0
    if max(a) - min(a) > ans:
        ans = max(a) - min(a)
    if max(b) - min(b) > ans:
        ans = max(b) - min(b)
    if max(c) - min(c) > ans:
        ans = max(c) - min(c)
    print(ans)


def __starting_point():
    main()


__starting_point()
