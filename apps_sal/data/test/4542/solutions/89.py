import itertools
s = input()
print(len(list(itertools.groupby(s))) - 1)
