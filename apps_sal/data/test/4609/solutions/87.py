import collections
n = int(input())
l = [input() for i in range(n)]
c = collections.Counter(l)
ans = 0
for (x, y) in c.items():
    if y % 2 != 0:
        ans += 1
print(ans)
