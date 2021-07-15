import itertools
pqr = list(map(int, input().split()))
print(min([a+b for a, b in itertools.combinations(pqr, 2)]))
