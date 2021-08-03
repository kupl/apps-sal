from collections import Counter
from sys import stdin
input = iter(stdin.readlines()).__next__

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ia = [0] * n
ib = [0] * n
for i, ai in enumerate(a):
    ia[ai - 1] = i
for i, bi in enumerate(b):
    ib[bi - 1] = i

diffs = [a_i - b_i for a_i, b_i in zip(ia, ib)]
for i, diff in enumerate(diffs):
    if diff < 0:
        diffs[i] = diff + n
counts = Counter(diffs)
print(counts.most_common(1)[0][1])
