from collections import Counter
S = str(input())
c = Counter(S)
d = c.most_common()
if len(d) == 2:
    ans = d[1][1] * 2
    print(ans)
else:
    print(0)
