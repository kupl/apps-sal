(n, k) = list(map(int, input().split()))

d = {}
a = []
for x in input().split():
    x = int(x)
    if not x in d:
        d[x] = 0
    d[x] += 1
    a.append(x)
    
lst = sorted(d)
lst.reverse()

d1 = {lst[0]: d[lst[0]]}
for x in range(1, len(lst)):
    d1[lst[x]] = d1[lst[x - 1]] + d[lst[x]]

array = [0] * n
for x in range(n):
    array[x] = n - d1[a[x]]

for x in range(k):
    (l, r) = list(map(int, input().split()))
    if a[l - 1] > a[r - 1]:
        array[l - 1] -= 1
    elif a[l - 1] < a[r - 1]:
        array[r - 1] -= 1

print(*array)

