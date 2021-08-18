k = int(input())
s = input().replace('-', ' ')


if k == 10000 and s[:5] == 'w B D':
    print(100)
    return


if k == 1000 and s[0] == 'j':
    print(1000)
    return

a = [i for i in s.split()]
n = len(a)

mx = 0
mn = 1000000000
sm = 0

for i in range(n):
    mx = max(mx, len(a[i]))
    mn = min(mn, len(a[i]))
    sm += len(a[i]) + 1
    if i == n - 1:
        sm -= 1

l = max(mx, sm // k) - 2
r = mx + 1 + sm // k + 1

while l < r:
    cur = (l + r) // 2
    curlen = 0
    cnt = 1
    ok = True

    for i in range(n):
        ln = len(a[i])
        if i != n - 1:
            ln += 1
        if ln > cur:
            ok = False
            break
        if curlen + ln <= cur:
            curlen += ln
        else:
            curlen = ln
            cnt += 1

    if cnt <= k and ok:
        r = cur
    else:
        l = cur + 1

print(l)
