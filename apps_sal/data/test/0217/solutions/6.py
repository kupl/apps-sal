a, b, f, k = list(map(int, input().split()))
now = b
path = 0
ans = 0
for i in range(k):
    if path == 0:
        if i == k - 1 and now >= a:
            break
        now -= f
        if now < 0:
            print(-1)
            return
        if 2 * (a - f) <= now:
            now -= a - f
        else:
            ans += 1
            now = b - (a - f)
        path = 1
    elif path == 1:
        if i == k - 1 and now >= a:
            break
        now -= a - f
        if now < 0:
            print(-1)
            return
        if 2 * f <= now:
            now -= f
        else:
            ans += 1
            now = b - f
        path = 0
if now < 0:
    print(-1)
    return
print(ans)
