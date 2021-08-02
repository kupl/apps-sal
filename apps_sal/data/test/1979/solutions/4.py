from collections import Counter

N = int(input())

A = [int(_) for _ in input().split()]
B = [int(_) for _ in input().split()]

posA = {}
for i, el in enumerate(A):
    posA[el] = i

cc = Counter()
for i, el in enumerate(B):
    diff = i - posA[el]
    if diff < 0:
        diff += N
    cc[diff] += 1

print(cc.most_common()[0][1])
