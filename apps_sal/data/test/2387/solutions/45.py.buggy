import sys
from operator import itemgetter
N = int(input())
S = sys.stdin.read().split()
HT_high = []
HT_low = []
for s in S:
    t = 0
    h = 0
    for c in s:
        if c == "(":
            h += 1
        else:
            h -= 1
            if h < t:
                t = h
    if h >= 0:
        HT_high.append((h, t))
    else:
        HT_low.append((h, t))
HT_high.sort(key=itemgetter(1), reverse=True)
HT_low.sort(key=lambda x: x[0] - x[1], reverse=True)
h0 = 0
for h, t in HT_high + HT_low:
    if h0 + t < 0:
        print("No")
        return
    h0 += h
if h0 != 0:
    print("No")
else:
    print("Yes")
