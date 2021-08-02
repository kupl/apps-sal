import sys
input = sys.stdin.readline


def root(k):
    while (k) != l[k]:
        k = l[l[k]]
    return(k)


n, m = list(map(int, input().split()))
l = [i for i in range(n + 1)]
sz = [1] * (n + 1)
maxnode = [i for i in range(n + 1)]
max_ = 0
for j in range(m):
    b, c = list(map(int, input().split()))
    max_ = max(max_, (max(b, c)))
    ro1 = root(b)
    ro2 = root(c)
    if c > maxnode[ro1]:
        maxnode[ro1] = c
    if b > maxnode[ro2]:
        maxnode[ro2] = b
    if ro1 != ro2:
        if sz[ro1] >= sz[ro2]:
            sz[ro1] += sz[ro2]
            sz[ro2] = 0
            l[ro2] = ro1
        else:
            sz[ro2] += sz[ro1]
            sz[ro1] = 0
            l[ro1] = ro2
# print(l,sz,maxnode)
end = 0
j = 0
while end < (max_):
    for k in range(end, n):
        if maxnode[k] > k:
            kj = maxnode[k]
            jk = max(maxnode[k:maxnode[k]])
            # print(jk,kj)
            while jk > kj:
                h = jk
                jk = max((maxnode[kj:jk]))
                kj = h
                # print(jk,kj)
            end = kj
            break
    # print(end)
    for i in range(kj, k - 1, -1):
        if l[root(i)] != root(k):
            l[root(i)] = root(k)
            j += 1
            # print(l[root(i)],(i),(k),j)
        # print(l)
print(j)
