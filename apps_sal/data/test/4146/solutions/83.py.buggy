from collections import Counter
import sys
n = int(input())
v = [[], []]
for i, j in enumerate(input().split()):
    if i & 1:
        v[0].append(int(j))
    else:
        v[1].append(int(j))

v1, v2 = Counter(v[0]), Counter(v[1])
mx1, mx2 = v1.most_common()[0], v2.most_common()[0]
if mx1[0] == mx2[0]:
    if mx1[1] + mx2[1] == n:
        print((n // 2))
        return
    nx1, nx2 = v1.most_common()[1][1], v2.most_common()[1][1]  # 次に最も多い数
    if nx1 > nx2:
        print((n - nx1 - mx2[1]))
    else:
        print((n - mx1[1] - nx2))
else:
    print((n - mx1[1] - mx2[1]))
