from collections import Counter
n = int(input())
v = list(map(int, input().split()))
(l, r) = (Counter(v[0::2]).most_common(), Counter(v[1::2]).most_common())
l.append((0, 0))
r.append((0, 0))
if l[0][0] != r[0][0]:
    print(n - (l[0][1] + r[0][1]))
else:
    print(min(n - (l[1][1] + r[0][1]), n - (l[0][1] + r[1][1])))
