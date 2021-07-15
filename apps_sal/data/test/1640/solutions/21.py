cnt = {}
n = int(input())
s = 0
an = 0
a = list(map(int, input().split()))
for i in range(n):
    if a[i] not in list(cnt.keys()):
        cnt[a[i]] = 0
    if a[i] - 1 not in list(cnt.keys()):
        cnt[a[i] - 1] = 0
    if a[i] + 1 not in list(cnt.keys()):
        cnt[a[i] + 1] = 0
    s += a[i]
    cnt[a[i]] += 1
    num = i + 1 - cnt[a[i]] - cnt[a[i] - 1] - cnt[a[i] + 1]
    an += num * a[i] - (s - a[i] * cnt[a[i]] - (a[i] + 1) * cnt[a[i] + 1] - (a[i] - 1) * cnt[a[i] - 1])
print(an)

