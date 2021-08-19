def main():
    (n, a, b) = [int(part) for part in input().split()]
    ghosts = []
    for i in range(n):
        ghosts.append([int(part) for part in input().split()])
    cnt = dict()
    vcnt = dict()
    for (x, vx, vy) in ghosts:
        if (vx, vy) in vcnt:
            vcnt[vx, vy] += 1
        else:
            vcnt[vx, vy] = 1
        tmp = vy - a * vx
        if tmp in cnt:
            cnt[tmp] += 1
        else:
            cnt[tmp] = 1
    ans = 0
    for (x, vx, vy) in ghosts:
        tmp = vy - a * vx
        ans += cnt[tmp] - vcnt[vx, vy]
    print(ans)


def __starting_point():
    main()


__starting_point()
