import time
import itertools


def main():
    N, M, R = tuple([int(x) for x in input().split()])

    r = [int(x) - 1 for x in input().split()]

    w_e = [tuple([int(x)for x in input().split()]) for _ in [0] * M]
    w_e = [(a - 1, b - 1, w) for (a, b, w) in w_e]

    g = Graph(list(range(N)), w_e)

    minimums = {}
    for r_i in r:
        minimums[r_i] = g.dijkstra(r_i)[0]

    bf = itertools.permutations(r)

    candidates = []
    for bf_i in bf:
        distance = 0
        for i in range(R - 1):
            distance += minimums[bf_i[i]][bf_i[i + 1]]
        candidates.append(distance)

    print(min(candidates))


def speedtest(func, *args):
    b = time.perf_counter()
    res = func(*args)
    e = time.perf_counter()
    elapsed = e - b
    print("{} (sec)".format(elapsed))

    return res


class Graph:
    def __init__(self, w_v, w_e):
        super().__init__()
        self.size = len(w_v)
        self.w_v = [v_i for v_i in w_v]
        self.w_e = [{} for _ in [0] * self.size]

        self.neighbor = [[] for _ in [0] * self.size]
        for a_i, b_i, w_i in w_e:
            self.w_e[a_i][b_i] = w_i
            self.w_e[b_i][a_i] = w_i

            self.neighbor[a_i].append(b_i)
            self.neighbor[b_i].append(a_i)

    def dijkstra(self, v_n):
        d = [-1] * self.size
        temp_d = [(10**9, i)for i in range(self.size)]
        temp_d[v_n] = (0, v_n)
        prev = [-1] * self.size

        q = set(range(self.size))

        while len(q) > 0:
            u = min([temp_d[q_i] for q_i in q])[1]
            d[u] = temp_d[u][0]
            q.discard(u)
            for v in self.neighbor[u]:
                temp = temp_d[u][0] + self.w_e[u][v]
                if temp_d[v][0] > temp:
                    temp_d[v] = temp, v
                    prev[v] = u

        return d, prev


def __starting_point():
    main()


__starting_point()
