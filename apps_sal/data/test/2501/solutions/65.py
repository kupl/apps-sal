n = int(input())
a = list(map(int, input().split()))
ipa = {}
ima = {}
for i in range(n):
    p = i + a[i]
    if p in ipa:
        ipa[p] += 1
    else:
        ipa[p] = 1
    m = i - a[i]
    if m in ima:
        ima[m] += 1
    else:
        ima[m] = 1
ans = 0
for k in ipa:
    if k in ima:
        ans += ipa[k] * ima[k]
print(ans)
