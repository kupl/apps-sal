from collections import defaultdict
from bisect import bisect
s = input()
S = len(s)
t = input()
T = len(t)
D = defaultdict(list)
Dc = defaultdict(int)
Exists = True
for i in range(S):
    D[s[i]].append(i + 1)
    Dc[s[i]] += 1
ans = 0
temp = 0
for i in range(T):
    if D[t[i]] == []:
        Exists = False
        break
    j = bisect(D[t[i]], temp)
    if j == Dc[t[i]]:
        ans += S - temp + D[t[i]][0]
        temp = D[t[i]][0]
    else:
        ans += D[t[i]][j] - temp
        temp = D[t[i]][j]
if Exists:
    print(ans)
else:
    print(-1)
