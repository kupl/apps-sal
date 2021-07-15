__author__ = 'PrimuS'

n, m, k = (int(x) for x in input().split())

order = [int(x) for x in input().split()]

touch = [int(x) for x in input().split()]

# n = 100000
# order = [0] * n
# k = 2
# m = 100000
# touch = [0] * n
# for i in range(n):
#     order[i] = i
# for i in range(m):
#     touch[i] = i

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
