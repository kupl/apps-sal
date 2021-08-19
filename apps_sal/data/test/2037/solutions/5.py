import sys
from collections import defaultdict
input = sys.stdin.readline
(n, m) = tuple(map(int, input().split()))
a = list(map(int, input().split()))
s = {}
dist = 0
ans = []
for t in a:
    if t in s and s[t] > 0:
        s[t] += 1
        ans.append(0)
    else:
        s[t] = 1
        dist += 1
        if dist == n:
            s = s
            ans.append(1)
            for k in list(s.keys()):
                s[k] -= 1
                if s[k] == 0:
                    dist -= 1
        else:
            ans.append(0)
print(''.join(list(map(str, ans))))
