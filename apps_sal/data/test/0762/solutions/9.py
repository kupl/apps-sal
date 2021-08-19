(q, w) = list(map(int, input().split()))
a = list(map(int, input().split()))
d = []
k = 0
for i in range(q - 1):
    k += a[i] % 2
    if k == i - k + 1:
        d.append(abs(a[i] - a[i + 1]))
d.sort()
k = 0
i = 0
while (i < len(d)) & (k <= w):
    k += d[i]
    i += 1
if k > w:
    print(i - 1)
else:
    print(i)
