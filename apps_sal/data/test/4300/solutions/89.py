from itertools import combinations
input()
d = list(map(int, input().split()))
comb = combinations(d, 2)
dsum = 0
for (a, b) in comb:
    dsum += a * b
print(dsum)
