def natlog(mx):
    maxpower = 0
    while mx > 1:
        mx = (mx+1) // 2
        maxpower += 1
    return maxpower

from collections import Counter
n = int(input())

if n == 1:
    print(1, 0)
    return

j = 2
setres  = Counter()

while n>1:
    if n % j == 0:
        n = n//j
        setres[j] += 1
    else:
        j+= 1

res = 1
for j in setres:
    res *= j
# print(res, setres, setres.most_common(1))
maxpower = natlog(setres.most_common(1)[0][1])
maxnum = 2**maxpower

cnt_actions = maxpower

for j, p in list(setres.items()):
    if p < maxnum:
        cnt_actions += 1
        break

print(res, cnt_actions)

