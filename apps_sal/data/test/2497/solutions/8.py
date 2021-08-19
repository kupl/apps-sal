import sys
inf = float('inf')


def solve(N: int, x: 'List[int]', y: 'List[int]', d: 'List[str]'):
    D_xmin = [inf for dd in [-1, 0, 1]]
    D_xmax = [-inf for dd in [-1, 0, 1]]
    D_ymin = [inf for dd in [-1, 0, 1]]
    D_ymax = [-inf for dd in [-1, 0, 1]]
    trans_x = {'U': 1, 'D': 1, 'L': 0, 'R': 2}
    trans_y = {'U': 2, 'D': 0, 'L': 1, 'R': 1}
    for (xx, yy, dd) in zip(x, y, d):
        D_xmin[trans_x[dd]] = min(D_xmin[trans_x[dd]], xx)
        D_xmax[trans_x[dd]] = max(D_xmax[trans_x[dd]], xx)
        D_ymin[trans_y[dd]] = min(D_ymin[trans_y[dd]], yy)
        D_ymax[trans_y[dd]] = max(D_ymax[trans_y[dd]], yy)
    ts = [0]
    for D in [D_xmin, D_xmax, D_ymin, D_ymax]:
        ts.append(D[0] - D[1])
        ts.append(D[1] - D[2])
        ts.append((D[0] - D[2]) / 2)
    res = inf
    for t in ts:
        if t < 0:
            continue
        xmin = min(D_xmin[0] - t, D_xmin[1], D_xmin[2] + t)
        xmax = max(D_xmax[0] - t, D_xmax[1], D_xmax[2] + t)
        ymin = min(D_ymin[0] - t, D_ymin[1], D_ymin[2] + t)
        ymax = max(D_ymax[0] - t, D_ymax[1], D_ymax[2] + t)
        res = min(res, (xmax - xmin) * (ymax - ymin))
    print(res)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    x = [int()] * N
    y = [int()] * N
    d = [str()] * N
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
        d[i] = next(tokens)
    solve(N, x, y, d)


def __starting_point():
    main()


__starting_point()
