from collections import defaultdict
n = int(input())
s = defaultdict(int)
t = defaultdict(int)

for i in range(n):
    x = input()
    s[x] += 1

m = int(input())
for i in range(m):
    x = input()
    t[x] += 1

ans = 0
for x, v in list(s.items()):
    now = v - t[x]
    ans = max(ans, now)

print(ans)
