import sys

#fin  = open("C.in", "r")
fin = sys.stdin

n = int(fin.readline())
A = []
for i in range(n):
    A += [fin.readline()[:-1]]

sg = {'(': +1, ')': -1}
INF = 2000000000


def analyze(s):
    sm = 0
    mn = 0
    for ch in s:
        sm += sg[ch]
        mn = min(mn, sm)

    if (sm >= 0 and mn < 0): return INF
    if (sm < 0 and sm != mn): return INF

    return sm


d = {}
for s in A:
    t = analyze(s)
    if (t == INF): continue

    if (t in d): d[t] += 1
    else: d[t] = 1

ans = 0
for a in d:
    if (a > 0 and (-a) in d): ans += min(d[a], d[-a])

if (0 in d): ans += d[0] // 2

print(ans)
