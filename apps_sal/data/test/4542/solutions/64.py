from itertools import groupby
S = input()
print(len(list(groupby(S))) - 1)
