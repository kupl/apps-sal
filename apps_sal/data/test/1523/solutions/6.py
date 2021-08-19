(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
d = {}
e = []
for i in range(n):
    if a[i] not in d:
        d[a[i]] = [b[i]]
    else:
        d[a[i]].append(b[i])
"\nprint(a)\nprint(b)\nprint('--------')\nprint(d)\n"
for i in d:
    if len(d[i]) > 1:
        d[i].pop(d[i].index(max(d[i])))
        e.extend(d[i])
e.sort()
'\nprint(d)\nprint(e)\n'
w = k - len(set(a))
print(sum(e[0:w]))
