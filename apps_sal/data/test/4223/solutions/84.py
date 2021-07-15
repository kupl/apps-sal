import itertools
n = int(input())
S = list(input())
L = [k for k, v in itertools.groupby(S)]
print(len(L))
