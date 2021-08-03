from collections import Counter
from itertools import combinations

N = int(input())
S = [input()[0] for _ in range(N)]
C = Counter(S)

ans = 0
for x, y, z in combinations("MARCH", 3):
    ans += C[x] * C[y] * C[z]

print(ans)
