s = input()
l = 0
r = len(s)
d = dict()
count = dict()
for i in s:
    d[i] = False
    count[i] = 0
while r - l > 1:
    mid = (r + l) // 2
    for i in s:
        d[i] = False
        count[i] = 0
    for i in range(mid):
        d[s[i]] = True
        count[s[i]] += 1
    for i in range(len(s) - mid):
        count[s[i]] -= 1
        count[s[i + mid]] += 1
        if count[s[i]] == 0:
            d[s[i]] = False
    for i in d.items():
        if i[1]:
            r = mid
    if r != mid:
        l = mid
print(r)
