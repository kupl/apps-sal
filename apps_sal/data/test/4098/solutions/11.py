import sys
from collections import Counter


def i_ints():
    return map(int, sys.stdin.readline().split())


(n, k) = i_ints()
c = Counter(i_ints())
c2 = dict()
a = sorted(c)
for i in sorted(a):
    c2[i] = sum((c[j] for j in range(i, i + 6)))
len_a = len(a)
next_group = [-1] * len(a)
for i in range(len_a):
    for j in range(i + 1, len_a):
        if a[j] > a[i] + 5:
            next_group[i] = j
            break
maxes = [0] * n
for ii in range(k):
    old_maxes = maxes
    old_maxes.append(0)
    maxes = []
    for (i, aa) in enumerate(a):
        maxes.append(c2[a[i]] + old_maxes[next_group[i]])
    m = 0
    for i in range(len(a) - 1, -1, -1):
        if maxes[i] > m:
            m = maxes[i]
        else:
            maxes[i] = m
print(max(maxes))
