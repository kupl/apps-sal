import sys
import numpy as np


def solve(N: int, T: 'List[int]', V: 'List[int]'):
    t_period = [0 for i in range(N + 1)]
    for i in range(N):
        t_period[i + 1] = t_period[i] + T[i] * 2
    limit = np.zeros((t_period[N] + 1,))
    for i in range(1, N):
        limit[t_period[i]] = min((V[i - 1], V[i]))
    for i in range(N):
        limit[t_period[i] + 1:t_period[i + 1]] = V[i]
    speed = np.zeros((t_period[N] + 1,))
    for v in range(1, 201):
        speed[1:t_period[N]] = np.min([limit[1:t_period[N]], speed[0:t_period[N] - 1] + 0.5, speed[2:t_period[N] + 1] + 0.5], axis=0)
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
