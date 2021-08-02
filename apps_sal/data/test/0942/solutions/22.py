n = int(input())
a = list(map(int, input().split()))
d = {}
l = [[] for i in range(n + 1)]
for i in range(n):
    d[a[i]] = d.get(a[i], 0) + 1
    l[n - a[i]].append(i + 1)
b = list(d.keys())
c = []
for i in b:
    c.append([d[i] // (n - i), n - i])
k = 0
for i in c:
    k += i[0] * i[1]
if k != n:
    print('Impossible')
else:
    print('Possible')
    co = 1
    ans = [0] * (n + 1)
    for i in c:
        for j in range(i[0]):
            for k in range(i[1]):
                x = l[i[1]].pop()
                ans[x] = co
            co += 1
    print(*ans[1:])
