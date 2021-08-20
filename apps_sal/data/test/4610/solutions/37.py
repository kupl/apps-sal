import collections as c
(n, k) = map(int, input().split())
x = list(map(int, input().split()))
y = c.Counter(x)
s = []
for i in y.items():
    s.append([i[1], i[0]])
s.sort()
ans = 0
for i in range(len(s) - k):
    ans += s[i][0]
print(ans)
