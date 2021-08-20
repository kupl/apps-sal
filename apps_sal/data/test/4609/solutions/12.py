from collections import defaultdict
d = defaultdict(int)
n = int(input())
for i in range(n):
    a = int(input())
    d[a] = int(not d[a])
ans = 0
for (k, v) in d.items():
    if v == 1:
        ans += 1
print(ans)
