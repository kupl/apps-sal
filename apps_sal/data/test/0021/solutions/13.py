def dist(l):
    return abs(l.index(1) - l.index(len(l)))


n = int(input())
l = list(map(int, input().split()))
one_ind = l.index(1)
n_ind = l.index(n)
d = dist(l)
for x in [one_ind, n_ind]:
    l[x], l[0] = l[0], l[x]
    d = max(d, dist(l))
    l[x], l[0] = l[0], l[x]

    l[x], l[-1] = l[-1], l[x]
    d = max(d, dist(l))
    l[x], l[-1] = l[-1], l[x]

print(d)
