import itertools
N = int(input())
S = list(input())
gr = list(itertools.groupby(S))
print(len(gr))
