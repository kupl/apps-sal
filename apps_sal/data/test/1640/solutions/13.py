n =int(input())
a = list(map(int, input().split()))
res , sum = 0, a[0]
cnt = dict()
cnt[a[0]] = 1
for i in range(1, n):
    res += a[i] * i - sum
    sum += a[i]
    if (a[i] - 1) in cnt:
        res -= cnt[a[i] - 1]
    if (a[i] + 1) in cnt:
        res += cnt[a[i] + 1]
    if a[i] not in cnt:
        cnt[a[i]] = 1
    else:
        cnt[a[i]] += 1
print(res)
