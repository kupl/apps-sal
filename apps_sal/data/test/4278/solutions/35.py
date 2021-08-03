n = int(input())
d = {}
e = []
ans = 0
for i in range(n):
    s = list(input())
    s.sort()
    s = "".join(s)
    if s in d:
        d[s] += 1
    else:
        d[s] = 1
for key, value in d.items():
    if value > 1:
        e.append(d[key])
for j in e:
    ans += j * (j - 1) // 2
print(ans)
