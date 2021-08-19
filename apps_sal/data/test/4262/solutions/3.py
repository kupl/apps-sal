import itertools
N = int(input())
P = tuple(map(int, input().split(' ')))
Q = tuple(map(int, input().split(' ')))
ls = [i for i in itertools.permutations(range(1, N + 1))]
a = [idx for (idx, val) in enumerate(ls) if val == P][0] + 1
b = [idx for (idx, val) in enumerate(ls) if val == Q][0] + 1
print(abs(a - b))
