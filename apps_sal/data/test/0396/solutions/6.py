(l, r) = input().split()
l = int(l)
r = int(r)
(a, b) = ([0] * 50, [0] * 50)
a[0] = 1
b[0] = 1
for i in range(1, 40):
    (a[i], b[i]) = (a[i - 1] * 2, b[i - 1] * 3)
ans = 0
for i in range(40):
    for j in range(40):
        if a[i] * b[j] >= l and a[i] * b[j] <= r:
            ans += 1
print(ans)
