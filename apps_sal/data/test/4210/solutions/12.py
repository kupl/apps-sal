(n, m) = list(map(int, input().split()))
arr = list(map(int, input().split()))
cnt = [0] * 12
for i in range(12):
    cnt[i] = {}
for i in range(n):
    t = arr[i]
    l = 0
    while t > 0:
        t = t // 10
        l += 1
    key = arr[i] % m
    if key in cnt[l]:
        cnt[l][key] += 1
    else:
        cnt[l][key] = 1
ans = 0
for i in range(n):
    t = arr[i]
    l = 0
    while t > 0:
        t = t // 10
        l += 1
    ky = arr[i] % m
    cnt[l][ky] -= 1
    mul = 10
    c = 1
    while c <= 11:
        key = (m - mul * arr[i] % m) % m
        if key in cnt[c]:
            ans += cnt[c][key]
        c += 1
        mul *= 10
    cnt[l][ky] += 1
print(ans)
