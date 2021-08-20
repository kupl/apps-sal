import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, t: 'List[int]', v: 'List[int]'):
    bounds = [[] for _ in range(N)]
    gb0 = (1, 0)
    tend = sum(t)
    gb1 = (-1, tend)
    for i in range(N):
        bounds[i].append(gb0)
        bounds[i].append(gb1)
    stt = 0
    for i in range(N):
        ti = t[i]
        vi = v[i]
        end = stt + ti
        b0 = (-1, stt + vi)
        b1 = (0, vi)
        b2 = (1, -end + vi)
        for j in range(i):
            bounds[j].append(b0)
        bounds[i].append(b1)
        for j in range(i + 1, N):
            bounds[j].append(b2)
        stt = end
    stt = 0
    vms = [0] * (tend * 2 + 1)
    for i in range(N):
        end = stt + t[i]
        bi = bounds[i]
        inf = float('inf')
        mins = {-1: inf, 0: inf, 1: inf}
        for (a, b) in bi:
            mins[a] = min(mins[a], b)
        for tm in range(stt * 2, end * 2):
            vms[tm] = min((a * tm + b * 2 for (a, b) in list(mins.items())))
        stt = end
    print(sum(vms) / 4)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    t = [int(next(tokens)) for _ in range(N)]
    v = [int(next(tokens)) for _ in range(N)]
    solve(N, t, v)


def __starting_point():
    main()


__starting_point()
