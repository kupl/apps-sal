n, m, k = list(map(int,input().split()))
p = list(map(int,input().split()))
s = list(map(int,input().split()))
c = list(map(int,input().split()))
sc = [0]*m
pt = [0]*m
add = 0
for i in range(m):
    ts = i + 1
    while ts in s:
        x = s.index(ts)
        if p[x] > sc[i]:
            sc[i] = p[x]
            pt[i] = x + 1
        s[x] = m + 1
for t in c:
    if t not in pt:
        add += 1
print(add)

