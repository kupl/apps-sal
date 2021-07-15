from collections import Counter

n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]

c = Counter(s).most_common()
d = Counter(t)

p = -1000

for k, v in c:
    p = max(p, v - d[k])

print(max(p, 0))
