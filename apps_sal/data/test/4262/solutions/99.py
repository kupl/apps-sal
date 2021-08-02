import itertools
n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))
permutation = list(itertools.permutations(range(1, n + 1)))
print(abs(permutation.index(p) - permutation.index(q)))
