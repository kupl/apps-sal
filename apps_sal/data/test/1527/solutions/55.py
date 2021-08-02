def main():
    H, W = [int(x) for x in input().split(" ")]
    S = []
    S.append(["X"] * (W + 2))
    h = 0
    w = 0
    for i in range(H):
        row = list(input())
        S.append(["X"] + row + ["X"])
        if not h and not w and row.count(".") > 0:
            h = i + 1
            w = row.index(".") + 1
    S.append(["X"] * (W + 2))

    ans = []
    for i in range(H):
        for j in range(W):
            ans.append(BFS(S, i + 1, j + 1, H + 2, W + 2))
    print((max(ans)))


def BFS(M, i, j, H, W):
    if M[i][j] != ".":
        return 0
    to_visit = [{"row": i, "col": j, "step": 0}]
    checked = [[0] * W for x in range(H)]
    checked[i][j] = 1
    z = [[0] * W for x in range(H)]
    while len(to_visit):
        visiting = to_visit.pop(0)
        r0 = visiting["row"]
        c0 = visiting["col"]
        s0 = visiting["step"]
        z[r0][c0] = s0
        for d in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            r = r0 + d[0]
            c = c0 + d[1]
            s = s0 + 1
            if checked[r][c] == 0 and M[r][c] == ".":
                to_visit.append({"row": r, "col": c, "step": s})
                checked[r][c] = 1
    a = 0
    for i in range(len(z)):
        for j in range(len(z[i])):
            if a < z[i][j]:
                a = z[i][j]
    return a


main()
