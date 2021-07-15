import itertools
N = int(input())
P = tuple(map(int, input().split(' ')))
Q = tuple(map(int, input().split(' ')))
ls = [ x for x in itertools.permutations(range(1, N + 1)) ]
a = [ key for key, val in enumerate(ls) if P == val ][0] + 1
b = [ key for key, val in enumerate(ls) if Q == val][0] + 1
print(abs(a - b))
