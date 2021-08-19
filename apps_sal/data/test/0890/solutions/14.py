from itertools import *
(n, l, r, x) = map(lambda x: int(x), input().split())
c = sorted(list(map(lambda x: int(x), input().split())))
variants = []
for i in range(2, n + 1):
    variants.extend(list(combinations(c, i)))
counter = 0
for i in range(len(variants)):
    sum_var = sum(variants[i])
    if sum_var >= l and sum_var <= r and (variants[i][-1] - variants[i][0] >= x):
        counter += 1
print(counter)
