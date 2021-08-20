from collections import defaultdict
from itertools import combinations
N = int(input())
D = defaultdict(int)
for _ in range(N):
    S = input()
    if S[0] in 'MARCH':
        D[S[0]] += 1
ans = 0
for C in combinations(('M', 'A', 'R', 'C', 'H'), 3):
    temp = 1
    for c in C:
        temp *= D[c]
    ans += temp
print(ans)
