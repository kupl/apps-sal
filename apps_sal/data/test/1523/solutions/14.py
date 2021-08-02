from collections import defaultdict


def delmax(lst):
    l = len(lst)
    if l == 0:
        return 0
    m = 0
    for i in range(l):
        v = lst[i]
        if v > m:
            m, n = v, i
    del lst[n]


n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
d = defaultdict(list)
for i in range(n):
    d[a[i]].append(b[i])

save = []
for key in d:
    u = d[key]
    delmax(u)
    save.extend(u)
save.sort(reverse=True)
del save[:n - k]
print(sum(save))
