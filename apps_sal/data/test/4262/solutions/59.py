import itertools
N = int(input())
perm = list(itertools.permutations(list(range(1, N + 1))))
a = tuple(list(map(int, input().split())))
b = tuple(list(map(int, input().split())))
print(abs(perm.index(a) - perm.index(b)))
