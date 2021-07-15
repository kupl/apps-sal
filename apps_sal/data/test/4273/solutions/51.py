from collections import Counter
from itertools import combinations
n = int(input())
s = [list(input())[0] for _ in range(n)]
c = Counter(s)
cnt = 0
listcmb = combinations("MARCH",3)

for k in listcmb:
    cnt += c[k[0]]*c[k[1]]*c[k[2]]
print(cnt)


