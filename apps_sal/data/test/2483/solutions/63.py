
import io
import sys
import math
from itertools import accumulate as acc

data = sys.stdin.readline

N, C = map(int, data().split())


array = [[0 for i in range(10**5 + 1)] for i in range(C + 1)]

rec = [0 for i in range(10**5 + 1)]

for i in range(N):
    s, t, c = map(int, data().split())
    recs, rect = array[c][s], array[c][t]
    if recs == 0 and rect == 0:
        rec[s - 1] += 1
        rec[t] -= 1
    elif recs == 0 and rect == 1:
        rec[s - 1] += 1
        rec[t - 1] -= 1
    elif recs == 1 and rect == 0:
        rec[s] += 1
        rec[t] -= 1
    elif recs == 1 and rect == 1:
        rec[s] += 1
        rec[t - 1] -= 1

    array[c][s], array[c][t] = 1, 1

tmp = 0
ans = 0
for i in range(10**5):
    tmp += rec[i]
    ans = max(tmp, ans)
print(ans)
