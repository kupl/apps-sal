(n, k, c) = map(int, input().split())
s = input()
cnt = 0
e = 0
l = []
for (i, si) in enumerate(s):
    if e == k:
        break
    if cnt > 0:
        cnt -= 1
        continue
    if si == 'o':
        l.append(i + 1)
        cnt = c
        e += 1
r = []
cnt = 0
d = 0
for (i, si) in enumerate(s[::-1]):
    if d == k:
        break
    if cnt > 0:
        cnt -= 1
        continue
    if si == 'o':
        r.append(n - i)
        cnt = c
        d += 1
for i in range(k):
    if l[i] == r[k - 1 - i]:
        print(l[i])
