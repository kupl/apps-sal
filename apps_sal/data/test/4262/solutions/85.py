import itertools
n = int(input())
(p, a, b) = (sorted(itertools.permutations(range(1, n + 1), n)), map(int, input().split()), map(int, input().split()))
print(abs(p.index(tuple(a)) - p.index(tuple(b))))
