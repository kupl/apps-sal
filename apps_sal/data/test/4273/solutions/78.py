import math
N = int(input())
first = 'MARCH'
dic = {s: 0 for s in first}
for _ in range(N):
    s = input()
    if s[0] in dic:
        dic[s[0]] += 1
t = []
for key in dic:
    if dic[key] > 0:
        t.append(dic[key])
if len(t) < 3:
    print(0)
else:
    tl = len(t)
    ans = 0
    for i in range(2 ** tl):
        cnt = []
        for j in range(tl):
            if i >> j & 1:
                cnt.append(j)
        if len(cnt) == 3:
            tans = 1
            for i in cnt:
                tans *= t[i]
            ans += tans
    print(ans)
