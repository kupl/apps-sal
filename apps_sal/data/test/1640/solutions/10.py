n = int(input())
a = list(map(int, input().split(' ')))

d = {}
s = a[0]
ret = 0
d[a[0]] = 1
for i in range(1, n):
    ret += a[i] * i - s
    if a[i] - 1 in d:
        ret -= d[a[i] - 1]
    if a[i] + 1 in d:
        ret += d[a[i] + 1]
    s += a[i]
    if a[i] not in d:
        d[a[i]] = 0
    d[a[i]] += 1

print(ret)
