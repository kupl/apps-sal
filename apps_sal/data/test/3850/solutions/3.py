import sys
from operator import itemgetter


def read(): return list(map(int, input().split()))


n, k, p = read()
people, keys = sorted(read()), sorted(read())

res = []
for i in range(k - n + 1):
    inner_res = []
    for j in range(n):
        inner_res.append(abs(keys[i + j] - people[j]) + abs(keys[i + j] - p))
    res.append(max(inner_res))

print(min(res))
