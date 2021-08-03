import itertools

n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

ls = list(itertools.permutations(range(1, n + 1)))

print(abs(ls.index(p) - ls.index(q)))
