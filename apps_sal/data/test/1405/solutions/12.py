n = int(input())
a = [int(i) for i in input().split()]
ans = a.count(0)
d, s = dict(), set(a)
for i in a:
    if i not in list(d.keys()):
        d[i] = 0
    d[i] += 1
for i in range(n):
    for j in range(n):
        if i == j or a[i] == a[j] == 0: continue
        a1, a2 = a[i], a[j]
        ln, dl = 2, [a1, a2]
        d[a1] -= 1
        d[a2] -= 1
        while a1 + a2 in s:
            a1, a2 = a2, a1 + a2
            d[a2] -= 1
            dl.append(a2)
            if d[a2] < 0:
                break
            ln += 1
        ans = max(ans, ln)
        for v in dl:
            d[v] += 1
print(ans)

