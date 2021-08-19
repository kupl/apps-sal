from collections import defaultdict
import string
n = int(input())
al = defaultdict(int)
old = defaultdict(int)
s = input()
for j in s:
    old[j] += 1
    al[j] += 1
for i in range(n - 1):
    s = input()
    d = defaultdict(int)
    for j in s:
        d[j] += 1
    for k in string.ascii_lowercase:
        al[k] = min(old[k], d[k], al[k])
    old = d
ans = ''
for k in string.ascii_lowercase:
    ans += k * al[k]
print(ans)
