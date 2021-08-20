from bisect import bisect_right
from operator import itemgetter
(s, b) = list(map(int, input().split()))
A = list(map(int, input().split()))
DG = [list(map(int, input().split())) for _ in range(b)]
DG.sort(key=itemgetter(0))
cumG = [0]
for (d, g) in DG:
    cumG.append(cumG[-1] + g)
D = list(map(itemgetter(0), DG))
Ans = []
for a in A:
    idx = bisect_right(D, a)
    Ans.append(cumG[idx])
print(*Ans)
