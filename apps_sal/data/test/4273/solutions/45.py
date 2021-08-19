from collections import defaultdict
from itertools import combinations


def inpl():
    return list(map(int, input().split()))


C = defaultdict(int)
N = int(input())
for _ in range(N):
    C[input()[0]] += 1
res = 0
for H in combinations('MARCH', r=3):
    res += C[H[0]] * C[H[1]] * C[H[2]]
print(res)
