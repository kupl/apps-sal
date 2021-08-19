(n, x) = list(map(int, input().split()))
a = list(map(int, input().split()))
d = {}
s = set(a)
for i in a:
    d[i] = 0
for i in a:
    d[i] += 1
ans = 0
for i in s:
    if x == 0:
        ans += d[i] * (d[i] - 1) // 2
    else:
        ans += d[i] * d.get(i ^ x, 0)
if x == 0:
    print(ans)
else:
    print(ans // 2)
