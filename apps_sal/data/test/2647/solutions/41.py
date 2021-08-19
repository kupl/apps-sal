def getval():
    h, w = map(int, input().split())
    s = [input() for i in range(h)]
    return h, w, s


def main(h, w, s):
    # Find numbers of whites
    whites = 0
    for i in s:
        for j in range(w):
            if i[j] == ".":
                whites += 1

    # Find the shortest path
    d = [[-1 for i in range(w)] for j in range(h)]
    q = [[0, 0, 0]]
    d[0][0] = 0
    while q:
        idx = q.pop(0)
        adj = [[idx[0] + 1, idx[1], idx[2] + 1], [idx[0] - 1, idx[1], idx[2] + 1], [idx[0], idx[1] + 1, idx[2] + 1], [idx[0], idx[1] - 1, idx[2] + 1]]
        for i in adj:
            if i[0] < 0 or i[1] < 0 or i[0] >= h or i[1] >= w:
                continue
            if d[i[0]][i[1]] != -1:
                continue
            if s[i[0]][i[1]] == "#":
                continue
            q.append(i)
            d[i[0]][i[1]] = i[2]

    dist = d[h - 1][w - 1]

    # Compute the score
    if dist == -1:
        print(-1)
    else:
        print(whites - dist - 1)


def __starting_point():
    h, w, s = getval()
    main(h, w, s)


__starting_point()
