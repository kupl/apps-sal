(n, b) = map(int, input().split())
a = list(map(int, input().split()))
(ce, co) = (0, 0)
d = []
for i in range(n - 1):
    if a[i] % 2 == 1:
        co += 1
    else:
        ce += 1
    if ce == co:
        d.append(abs(a[i] - a[i + 1]))
d.sort()
res = 0
for i in range(len(d)):
    if b >= d[i]:
        res += 1
        b -= d[i]
print(res)
