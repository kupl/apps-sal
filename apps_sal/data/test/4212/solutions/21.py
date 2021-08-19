import copy


def main():
    N, M, Q = [int(n) for n in input().split(" ")]
    q = [[int(a) for a in input().split(" ")] for i in range(Q)]
    all_series = get_series(N, M)
    points = [0]
    for l in all_series:
        points.append(get_score(l, q))
    print(max(points))


def get_score(l, q):
    return sum([q[i][3] if l[q[i][1] - 1] - l[q[i][0] - 1] == q[i][2] else 0 for i in range(len(q))])


def get_series(N, M):
    # N: number of elms
    # M: upper limit of val of elm
    all_series = []
    checked = [[0] * M for i in range(N)]
    to_check = [[0, j + 1] for j in range(M)]
    series = [0 for k in range(N)]
    while len(to_check) > 0:
        checking = to_check.pop(-1)
        series[checking[0]] = checking[1]
        if checking[0] == N - 1:
            l = copy.deepcopy(series)
            all_series.append(l)
        else:
            to_check.extend([[checking[0] + 1, k] for k in range(checking[1], M + 1)])
    return all_series


main()
