from itertools import combinations
n = int(input())
d = list(map(int, input().split()))
comb = combinations(d, 2)
res = 0
for (x, y) in comb:
    res += x * y
print(res)
