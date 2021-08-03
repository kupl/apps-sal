n = int(input())
s_l = [input() for _ in range(n)]

d = {}
for i in list(s_l[0]):
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
c_l = set(list(s_l[0]))


for s in s_l[1:]:
    for c in list(c_l):
        count = list(s).count(c)
        if d[c] > count:
            d[c] = count

ans = []
for k in list(c_l):
    for _ in range(d[k]):
        ans.append(k)
ans = sorted(ans)
ans2 = ''
for a in ans:
    ans2 += a
print(ans2)
