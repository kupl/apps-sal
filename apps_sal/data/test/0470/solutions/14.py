t = list(map(int, input().split()))
s = sum(t)
ans = s
for i in range(5):
    c = t.count(t[i])
    if c >= 2:
       ans = min(s - min(c, 3) * t[i], ans)
print(ans)
