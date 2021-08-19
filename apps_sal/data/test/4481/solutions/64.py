# C
from collections import Counter
N = int(input())
S = [input() for _ in range(N)]
countS = Counter(S)
maxS = max(countS.values())
ans = []
for key, value in list(countS.items()):
    if value == maxS:
        ans.append(key)

for a in sorted(ans):
    print(a)
