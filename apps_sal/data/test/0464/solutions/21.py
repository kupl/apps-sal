H, W = list(map(int, input().split()))
X = [[[0, 1][a == "*"] for a in input()] for i in range(H)]


def main():
    s = sum([sum(x) for x in X])
    # print(X, s)

    h, w = -1, -1
    for i in range(H):
        for j in range(W):
            if X[i][j]:
                w = j
                break
        if w >= 0:
            break
    else:
        return 0

    for j in range(W):
        for i in range(H):
            if X[i][j]:
                h = i
                break
        if h >= 0:
            break
    else:
        return 0

    if X[h][w] == 0:
        return 0

    c = 1
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        # print(di, dj)
        i, j = h, w
        # print("h, w =", h, w)
        if 0 <= i + di < H and 0 <= j + dj < W:
            if X[i + di][j + dj] == 0:
                return 0
        else:
            return 0

        while 0 <= i + di < H and 0 <= j + dj < W:
            i += di
            j += dj
            # print("--", i,j)
            if X[i][j] == 0:
                break
            # print("i, j =", i, j)
            c += 1
    # print(s, c)
    if s == c:
        return 1
    return 0


if main():
    print("YES")
else:
    print("NO")
