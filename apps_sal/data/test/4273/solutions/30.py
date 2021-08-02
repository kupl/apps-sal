import itertools
from collections import Counter

N = int(input())
S = Counter([input()[0] for i in range(N)])
res = 0
for a, b, c in itertools.combinations("MARCH", 3):
    res += S[a] * S[b] * S[c]

print(res)
