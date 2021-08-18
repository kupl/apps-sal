
n = int(input())
s = [input() for _ in range(n)]

d = {}
for i in range(len(s[0])):
    if s[0][i] not in d:
        d[s[0][i]] = 1
    else:
        d[s[0][i]] += 1

for i in range(n):
    for key in list(d.keys()):
        tmp = 0
        for k in range(len(s[i])):
            if s[i][k] == key:
                tmp += 1
        if tmp <= d[key]:
            d[key] = tmp

d = sorted(list(d.items()), key=lambda x: x[0])
ans = ''
for i in range(len(d)):
    for _ in range(d[i][1]):
        ans += d[i][0]
print(ans)
