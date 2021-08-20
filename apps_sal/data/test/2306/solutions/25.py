import sys
import numpy as np


def solve(N: int, T: 'List[int]', V: 'List[int]'):
    t_period = [0 for i in range(N + 1)]
    for i in range(N):
        t_period[i + 1] = t_period[i] + T[i] * 2
    V = [0] + V + [0]
    limit = np.zeros((N + 2, t_period[N] + 1))
    line = np.arange(0, t_period[N] / 2 + 0.5, 0.5)
    for i in range(N + 2):
        if i == 0:
            (l, r) = (0, 0)
        elif i == N + 1:
            (l, r) = (t_period[N], t_period[N])
        else:
            (l, r) = (t_period[i - 1], t_period[i])
        limit[i] = np.max([-line + l * 0.5, line * 0, line - r * 0.5], axis=0) + V[i]
    speed = np.min(limit, axis=0)
    total = 0
    for t in range(t_period[N]):
        total += (speed[t] + speed[t + 1]) * 0.5 * 0.5
    print(total)
    return


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
