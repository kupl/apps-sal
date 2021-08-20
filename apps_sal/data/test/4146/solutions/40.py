from collections import Counter
n = int(input())
ls = list(map(int, input().split()))
lso = ls[::2]
lse = ls[1::2]
lso.sort()
lse.sort(reverse=True)
co = Counter(lso)
ce = Counter(lse)
(co1, co2) = (co.most_common()[0][0], co.most_common()[0][1])
(ce1, ce2) = (ce.most_common()[0][0], ce.most_common()[0][1])
(coo1, coo2, cee1, cee2) = (0, 0, 0, 0)
if co2 != n // 2:
    (coo1, coo2) = (co.most_common()[1][0], co.most_common()[1][1])
if ce2 != n // 2:
    (cee1, cee2) = (ce.most_common()[1][0], ce.most_common()[1][1])
if co1 == ce1:
    print(n - max(co2 + cee2, ce2 + coo2))
else:
    print(n - co2 - ce2)
