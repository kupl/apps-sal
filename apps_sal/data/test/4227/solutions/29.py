from itertools import permutations, islice


def window(seq, n):
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result


N, M, *ab = list(map(int, open(0).read().split()))
g = [[0] * N for _ in range(N)]
for a, b in zip(*[iter(ab)] * 2):
    g[a - 1][b - 1] = 1
    g[b - 1][a - 1] = 1

ans = 0
for path in permutations(list(range(1, N))):
    path = [0] + list(path)
    if all(g[v][nv] for v, nv in window(path, 2)):
        ans += 1
print(ans)

