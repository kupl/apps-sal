from collections import Counter
from string import ascii_lowercase
n = int(input())
s = {ai: float("INF") for ai in ascii_lowercase}

for i in range(n):
    si = input()
    c = Counter(si)
    for k in ascii_lowercase:
        s[k] = min(s[k], c[k])

ans = ""
for key in ascii_lowercase:
    ans += key * s[key]
print(ans)
