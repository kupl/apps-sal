from itertools import groupby

n = int(input())
a = sorted([int(x) for x in input().strip().split()], reverse=True)
b = [len([ci for ci in c]) for g, c in groupby(a)]

all_even = True
for bi in b:
    if bi & 1:
        all_even = False
        break

print('Conan' if not all_even else 'Agasa')
