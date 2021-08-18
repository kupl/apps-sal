def power(a, p):
    if p == 0:
        return 1
    lol = power(a, p // 2)
    lol = lol * lol
    if p % 2 == 1:
        return a * lol
    else:
        return lol


x, y, l, r = map(int, input().split())

i = 0
d = {}

while 1:
    k = power(x, i)
    j = 0
    if k > r:
        break
    while 1:
        lol = power(y, j)
        if k + lol > r:
            break
        d[k + lol] = 1
        j += 1
    i += 1
last = l - 1
d[r + 1] = 1
arr = []
for k in d.keys():
    arr.append(k)
ans = 0
arr.sort()
for k in arr:
    if k >= l:
        ans = max(ans, k - last - 1)
        last = k
        if last >= r:
            break
print(ans)
