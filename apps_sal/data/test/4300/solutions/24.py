import itertools
N = int(input())
d = list(map(int, input().split()))

lst = list(itertools.combinations(d, 2))
total = 0
for n in lst:
    c = n[0] * n[1]
    total += c
print(total)
