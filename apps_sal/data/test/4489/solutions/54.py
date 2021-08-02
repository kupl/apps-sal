from collections import Counter
n = int(input())
s = Counter([input() for _ in range(n)])
m = int(input())
t = Counter([input() for _ in range(m)])

for x, y in s.items():
    s[x] = s[x] - t[x]
print(max(max(list(s.values())), 0))
