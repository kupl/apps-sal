import sys
(w, l) = [int(x) for x in input().split()]
use = [int(x) for x in input().split()]
m = sum(use[0:l])
s = m
for i in range(1, w - l):
    s = s - use[i - 1] + use[i + l - 1]
    if s < m:
        m = s
print(m)
'\nimport sys\n\nw, l = [int(x) for x in input().split()]\nuse = [int(x) for x in input().split()]\nuse.append(sys.maxsize)\ncount = [0] * (w + 1)\ncount[0] = 1\n\nfor i in range(1, w+1):\n    count[i] = min(sum(count[max(i-l,0):i]), use[i-1])\n\nprint(count[-1])\n'
