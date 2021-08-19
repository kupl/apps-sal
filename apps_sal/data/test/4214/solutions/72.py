import itertools
import math


def calc_kyori(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


N = int(input())
l = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    l.append(tmp)
total = 0
comb = 0
for i in list(itertools.permutations(list(range(N)))):
    comb += 1
    for j in range(N - 1):
        total += calc_kyori(l[i[j]], l[i[j + 1]])
print(total / comb)
