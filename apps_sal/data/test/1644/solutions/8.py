n = int(input())
d = []
for i in range(n):
    (a, b, h) = map(int, input().split())
    d.append((b, a, h))
d.sort()
ht = d[len(d) - 1][2]
ans = ht
s = []
s.append(d[len(d) - 1])
for i in range(n - 2, -1, -1):
    while s and d[i][0] <= s[len(s) - 1][1]:
        ht -= s.pop()[2]
    s.append(d[i])
    ht += d[i][2]
    if ans < ht:
        ans = ht
print(ans)
