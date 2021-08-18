__author__ = 'PrimuS'

n, m, k = (int(x) for x in input().split())

order = [int(x) for x in input().split()]

touch = [int(x) for x in input().split()]


res = 0
d = {}

for i in range(n):
    d[order[i]] = i

for x in touch:
    pos = d[x]
    res += pos // k + 1
    if pos > 0:
        order[pos - 1], order[pos] = order[pos], order[pos - 1]
        d[x] = pos - 1
        d[order[pos]] = pos

print(res)
