import collections as c
n = int(input())
s = []
ans = 0
for i in range(n):
    t = list(input())
    t.sort()
    t = str(t)
    s.append(t)
s = c.Counter(s)
for i in s.values():
    ans += i * (i - 1) // 2
print(ans)
