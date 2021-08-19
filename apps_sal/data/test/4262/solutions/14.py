import itertools
n = int(input())
p = tuple([int(s) for s in input().split()])
q = tuple([int(s) for s in input().split()])
lst = list(itertools.permutations(list(range(1, n + 1))))
print(abs(lst.index(p) - lst.index(q)))
