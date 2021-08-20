n = int(input())
l = [int(j) for j in input().split()]
d = dict()
pre = []
for i in range(n):
    if l[i] in d:
        d[l[i]] += 1
    else:
        d[l[i]] = 1
    pre.append(d[l[i]])
suf = [0 for i in range(n)]
d = dict()
for i in range(n - 1, -1, -1):
    if l[i] in d:
        d[l[i]] += 1
    else:
        d[l[i]] = 1
    suf[i] = d[l[i]]


def update(bit, index, val):
    n = len(bit)
    while index < n:
        bit[index] += val
        index += index & -1 * index


def getsum(bit, index):
    n = len(bit)
    ans = 0
    while index > 0:
        ans += bit[index]
        index -= index & -1 * index
    return ans


n = len(pre)
bit = [0] * (max(suf) + 1)
inv_ct = 0
for i in range(n - 1, -1, -1):
    inv_ct += getsum(bit, pre[i] - 1)
    update(bit, suf[i], 1)
print(inv_ct)
