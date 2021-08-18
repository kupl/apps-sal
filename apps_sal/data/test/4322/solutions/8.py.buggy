n = int(input())

a = [int(x) for x in input().split()]

if n == 1:
    print(1)
    print(a[0])
    return

a.sort()

b = [a[0]]
cnt = [0] * (200 * 1000 + 1)

cnt[a[0]] += 1
for i in range(1, n):
    cnt[a[i]] += 1
    if a[i - 1] != a[i]:
        b.append(a[i])

l = 0
r = 1
ans = cnt[a[0]]

i = 0
while i < len(b):
    j = i + 1
    su = cnt[b[i]]
    while j < len(b) and b[j] - b[j - 1] == 1 and cnt[b[j]] >= 2:
        su += cnt[b[j]]
        j += 1
    tmp = j
    if j < len(b) and b[j] - b[j - 1] == 1:
        su += cnt[b[j]]
        j += 1
    if ans < su:
        ans = su
        l = i
        r = j
    i = tmp


print(ans)
for i in range(l, r):
    print(b[i], end=' ')
for i in range(r - 1, l - 1, -1):
    for j in range(0, cnt[b[i]] - 1):
        print(b[i], end=' ')
