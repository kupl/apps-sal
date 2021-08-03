from itertools import combinations
n = int(input())
d = list(map(int, input().split()))
c = combinations(d, 2)
sumd = 0
for x, y in c:
    sumd += x * y
print(sumd)
