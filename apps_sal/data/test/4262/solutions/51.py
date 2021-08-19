import itertools
N = int(input())
perm = [x for x in itertools.permutations(range(1, N + 1))]
P = tuple(map(int, input().split(' ')))
Q = tuple(map(int, input().split(' ')))
a = [idx for (idx, val) in enumerate(perm) if val == P][0] + 1
b = [idx for (idx, val) in enumerate(perm) if val == Q][0] + 1
print(abs(a - b))
