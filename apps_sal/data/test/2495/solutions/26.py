n = int(input())
a = list(map(int, input().split()))
now = a[0]
if now == 0:
    ans = 1
    now = 1
else:
    ans = 0
for i in a[1:]:
    t = now + i
    if now * t >= 0:
        if now >= 0:
            ans += t + 1
            now = -1
        else:
            ans += 1 - t
            now = 1
    else:
        now = t
if a[0] >= 0:
    now = -1
    ans2 = a[0] - now
else:
    now = 1
    ans2 = now - a[0]
for i in a[1:]:
    t = now + i
    if now * t >= 0:
        if now >= 0:
            ans2 += t + 1
            now = -1
        else:
            ans2 += 1 - t
            now = 1
    else:
        now = t
ans = min(ans, ans2)
print(ans)
