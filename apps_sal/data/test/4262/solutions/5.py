import itertools

n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))
P = tuple(itertools.permutations(range(1, n + 1)))

print(abs(P.index(p) - P.index(q)))
