import collections

n = int(input())
m = n // 2
a = list(map(int, input().split()))
g = []
k = []
for x in range(n):
    if (x + 1) % 2 == 1:
        k.append(a[x])
    else:
        g.append(a[x])

gg = collections.Counter(g)
kk = collections.Counter(k)
aa = collections.Counter(a)

if len(aa) == 1:
    print((n // 2))

else:
    if gg.most_common()[0] == kk.most_common()[0]:

        print((min(m - gg.most_common()[0][1] + m - kk.most_common()[1][1], m - kk.most_common()[0][1] + m - gg.most_common()[1][1])))

    else:
        print((n - gg.most_common()[0][1] - kk.most_common()[0][1]))
