import itertools
N = int(input())
P = tuple([int(i) for i in input().split()])
Q = tuple([int(i) for i in input().split()])
perm = sorted(list(itertools.permutations(P)))
print(abs(perm.index(P)-perm.index(Q)))
