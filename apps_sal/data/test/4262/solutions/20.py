import itertools
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
p = list(itertools.permutations(range(1, N + 1)))
a = p.index(P)
b = p.index(Q)
print(abs(a - b))
