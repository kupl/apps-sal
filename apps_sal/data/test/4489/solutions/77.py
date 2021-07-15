n = int(input())
s=[]
for i in range(n):
    s.append(input())
from collections import Counter
cs = Counter(s)
m = int(input())
for i in range(m):
    t = input()
    if cs[t]:
        cs[t] -= 1
print(cs.most_common(1)[0][1], flush=True)


