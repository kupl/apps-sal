import sys
import collections as cc
input = sys.stdin.readline


def I():
    return list(map(int, input().split()))


s = input().strip()
f = cc.defaultdict(list)
f['a'] = [0, 0]
f['b'] = [0, 0]
od = 0
ev = 0
for i in range(len(s)):
    if i % 2 == 0:
        od += f[s[i]][0]
        ev += f[s[i]][1]
    else:
        od += f[s[i]][1]
        ev += f[s[i]][0]
    f[s[i]][i % 2] += 1
print(ev, od + len(s))
