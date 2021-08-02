from collections import Counter, defaultdict
import bisect

s = input()
t = input()
ss = s * 2

S = Counter(s)
T = Counter(t)

for i in T.keys():
    if i not in S:
        print(-1)
        return

alpha = [[] for _ in range(26)]

for i, j in enumerate(ss):
    alpha[ord(j) - ord("a")].append(i)

rep, now = 0, -1

for i in t:
    alp = alpha[ord(i) - ord('a')]
    i = bisect.bisect_left(alp, now + 1)
    now = alp[i]
    if now >= len(s):
        now -= len(s)
        rep += 1

print(rep * len(s) + now + 1)
