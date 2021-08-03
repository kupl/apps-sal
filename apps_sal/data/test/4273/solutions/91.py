from itertools import combinations
from collections import Counter

N = int(input())
S = Counter()

for i in range(N):
    S[input()[0]] += 1

tmp = []
for a, b, c in combinations('MARCH', 3):
    tmp.append(int((S[a] * S[b] * S[c])))

print((sum(tmp)))
