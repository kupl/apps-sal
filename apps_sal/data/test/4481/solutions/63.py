from collections import Counter

n = int(input())
s = [input() for _ in range(n)]

c = Counter(s)
m = c.most_common()[0][1]
k = list(c.keys())
v = list(c.values())

l = []
for i in range(len(c)):
  if v[i] == m:
    l.append(k[i])

l.sort()
    
print(*l,sep="\n")
