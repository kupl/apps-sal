import itertools
import collections


f = lambda p: sum(itertools.starmap(lambda i, j: min(p[i: j + 1]), itertools.combinations_with_replacement(list(range(n)), 2)))

n, m = list(map(int, str.split(input())))
mem = collections.defaultdict(list)
for p in itertools.permutations(list(range(1, n + 1)), n):

    mem[f(p)].append(p)

print(str.join(" ", list(map(str, mem[max(mem)][m - 1]))))

