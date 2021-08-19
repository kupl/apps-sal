from collections import defaultdict
d = defaultdict(int)
n = int(input())
for i in range(n):
    a = int(input())
    if d[a] > 0:
        d[a] -= 1
    else:
        d[a] += 1
ans = 0
for v in list(d.values()):
    if v > 0:
        ans += 1
print(ans)
