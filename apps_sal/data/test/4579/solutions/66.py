# C
from collections import Counter

N = int(input())
S = [input() for _ in range(N)]

counter = Counter(S)

print((len(list(counter.keys()))))
