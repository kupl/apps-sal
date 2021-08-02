n, *a = map(int, open(0).read().split())
pre1 = 0
pre2 = 0
ans1 = 0
ans2 = 0
for i in range(n):
    x = (-1)**(i % 2)
    y = -x
    pre1 += a[i]
    pre2 += a[i]
    if x * pre1 <= 0:
        ans1 += abs(pre1 - x)
        pre1 = x
    if y * pre2 <= 0:
        ans2 += abs(pre2 - y)
        pre2 = y
print(min(ans1, ans2))
