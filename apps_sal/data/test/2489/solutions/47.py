n = int(input())
a = list(map(int, input().split()))
a.sort()
d = {}
for x in a:
    d[x] = d.get(x, 0) + 1
ans = 0
ok = [1] * (10 ** 6 + 1)
for x in list(d.keys()):
    if ok[x]:
        for j in range(2, 10 ** 6 // x + 1):
            ok[j * x] = 0
        if d[x] == 1:
            ans += 1
print(ans)
