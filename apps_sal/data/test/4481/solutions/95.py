import collections
n = int(input())
names = [input() for _ in range(n)]
c = collections.Counter(names)
maxv = max(c.values())
ans = []
for i in c.items():
    if i[1] == maxv:
        ans.append(i[0])
ans = sorted(ans)
for i in ans:
    print(i)
