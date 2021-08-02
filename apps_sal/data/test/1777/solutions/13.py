n = int(input())

d = {}

for i in range(n):
    s = input()
    k = 0
    pr = True
    suf = True
    for j in s:
        if j == '(':
            k += 1
        else:
            k -= 1
        if k < 0:
            pr = False
    k = 0
    for j in reversed(s):
        if j == '(':
            k += 1
        else:
            k -= 1
        if k > 0:
            suf = False
    if (k > 0 and pr) or (k == 0 and pr and suf) or (k < 0 and suf):
        if k not in d:
            d[k] = 0
        d[k] += 1

ans = 0
if 0 in d:
    ans += d[0] // 2
    del d[0]
for k in d:
    if d[k] <= 0:
        continue
    if -k in d and d[-k] > 0:
        mn = min(d[k], d[-k])
        d[k] -= mn
        d[-k] -= mn
        ans += mn
print(ans)
