import itertools
a = list(map(int, input().split()))
res = sum(a)
for i in itertools.permutations(a):
    (a1, a2, a3) = i
    tmp = abs(a1 - a2) + abs(a2 - a3)
    res = min(res, tmp)
print(res)
