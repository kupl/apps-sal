n, k = map(int, input().split())
a = list(map(int, input().split()))
d = {}
for i in range(1, n+1):
    d[i] = 0
l = [1]
x = 1
if n >= k:
    for i in range(k):
        x = a[x-1]
    print(x)
    return
for i in range(n):
    x = a[x-1]
    if d[x] == 1:
        k -= l.index(x)
        print(l[l.index(x):][k%(l.index(x)-len(l))])
        return
    l.append(x)
    d[x] += 1
print(x)
