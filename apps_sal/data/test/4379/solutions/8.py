n = int(input())
a = [int(s) for s in input().split()]
lens = {}
maxlen = 1
maxlast = a[0]
for i in range(n):
    lens[a[i]] = lens.get(a[i]-1, 0) + 1
    if lens[a[i]] > maxlen:
        maxlen = lens[a[i]]
        maxlast = a[i]
# print(lens)
# print(maxlast, maxlen)
print(maxlen)
subs = []
si = maxlast - maxlen + 1
for i in range(n):
    if a[i] == si:
        subs.append(i+1)
        si += 1
print(*subs, sep=' ')
