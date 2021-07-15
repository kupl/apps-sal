from itertools import groupby
S = input()
gr = groupby(S)
print((len(list(gr))-1))

