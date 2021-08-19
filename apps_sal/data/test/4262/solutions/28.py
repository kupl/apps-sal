import itertools
n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))
a = list(itertools.permutations(list(range(1, n + 1))))
(pp, qq) = (0, 0)
for (i, j) in enumerate(a):
    if p == j:
        pp = i
    if q == j:
        qq = i
print(abs(pp - qq))
