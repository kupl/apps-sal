import itertools
n, m = map(int, input().split())
i = [2] * n
j = [2] * m
p = list(itertools.combinations(i, 2))
q = list(itertools.combinations(j, 2))
print(len(p) + len(q))
