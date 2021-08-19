from itertools import groupby
print(sum((1 for (k, g) in groupby(input()) if len(list(g)) % 2 == 0)))
