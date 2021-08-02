n, k = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))
s = []
for i in range(n):
    s.append([i, p[i], c[i]])
s.sort(key=lambda x: x[1])
tk = 0
m = []
for i in range(n):
    coin = s[i][2] + sum(m)
    s[i].append(coin)
    if tk < k:
        m.append(s[i][2])
        tk += 1
    elif len(m) > 0:
        if min(m) < s[i][2]:
            m.remove(min(m))
            m.append(s[i][2])
s.sort()
for a in s:
    print(a[3], end=' ')
