n = int(input())
a = list(map(int, input().split()))
d = {}
for i in range(n):
    if d.get(a[i]) == None:
        d[a[i]] = 1
    else:
        d[a[i]] += 1
count = 0
used = set()
for i in range(n):
    d[a[i]] -= 1
    if d[a[i]] == 0:
        del d[a[i]]
    if a[i] not in used:
        count += len(d)
    used.add(a[i])
print(count)

