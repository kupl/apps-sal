from collections import defaultdict
import bisect
import sys
readline = sys.stdin.readline

S = readline().rstrip()
T = readline().rstrip()

if len(set(T) - set(S)) > 0:
    print(-1)
    return

S2 = S * 2
dic = defaultdict(list)

for i in range(len(S2)):
    dic[S2[i]] += [i]

ind = -1
ans = 0
for t in T:
    targets = dic[t]
    newind = targets[bisect.bisect_left(targets, ind + 1)]
    ans += (newind - ind)
    if newind >= len(S):
        newind -= len(S)
    ind = newind

print(ans)
