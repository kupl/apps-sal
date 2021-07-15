S = input()
from collections import defaultdict as dd
Hand = dd(lambda:0)
for s in S:
    Hand[s] += 1
ans = len(S)//2 - Hand['p']
print(ans)
