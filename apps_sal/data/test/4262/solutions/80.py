import itertools
N = int(input())
P = tuple(map(int, input().split(' ')))
Q = tuple(map(int, input().split(' ')))
ls = [x for x in itertools.permutations(range(1, N + 1), N)]
a = [key for (key, val) in enumerate(ls) if val == P][0] + 1
b = [key for (key, val) in enumerate(ls) if val == Q][0] + 1
print(abs(a - b))
