from collections import Counter
n = int(input())
s = list(input() for i in range(n))
c = Counter(s)
m = max(c.values())
s = sorted(list(set(s)))
for i in range(len(s)):
    if c[s[i]] == m:
        print(s[i])
