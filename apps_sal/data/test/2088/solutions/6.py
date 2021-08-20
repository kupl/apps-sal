import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
P = list(map(int, input().split()))
LIST = [0] * (n + 1)
LEAF = [1] * (n + 1)
for p in P:
    LEAF[p] = 0
for i in range(1, n + 1):
    if LEAF[i] == 1:
        LIST[i] = 1
for i in range(n, 1, -1):
    LIST[P[i - 2]] += LIST[i]
counter = Counter(LIST[1:])
SUM = [0]
SC = sorted(counter.keys())
for j in SC:
    SUM.append(SUM[-1] + counter[j])
i = 1
j = 0
while j < len(SUM):
    if i <= SUM[j]:
        print(SC[j - 1], end=' ')
    else:
        j += 1
        continue
    i += 1
