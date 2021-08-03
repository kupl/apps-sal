import numpy as np


def solve(string):
    n, k, *xyc = string.split()
    k = int(k)
    l = 2 * int(k)
    xy = [(int(x) % l, int(y) % l) if c == "W" else (int(x) % l, (int(y) + k) % l)
          for x, y, c in zip(xyc[::3], xyc[1::3], xyc[2::3])]
    ans = [[0 for j in range(l + 0)] for i in range(l + 0)]
    for _x, _y in xy:
        if (_x - k + 0.5) * (_y - k + 0.5) > 0:
            lt = 2
            lte = 1
            ans[0][0] += 1
        else:
            lt = -2
            lte = -1
        _x %= k
        _y %= k
        ans[_x][_y] += lt
        ans[_x + k][_y] -= lt
        ans[_x][_y + k] -= lt
        ans[_x + k][_y + k] += lt
        ans[_x + k][0] += lte
        ans[0][_y + k] += lte
        ans[_x][0] -= lte
        ans[0][_y] -= lte
    return str(np.asarray(ans).cumsum(axis=1).cumsum(axis=0).max())


def __starting_point():
    n, m = list(map(int, input().split()))
    print((solve('{} {}\n'.format(n, m) + '\n'.join([input() for _ in range(n)]))))


__starting_point()
