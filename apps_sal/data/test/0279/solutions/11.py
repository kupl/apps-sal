w1, w2 = list(map(int, input().split()))
t, d = list(map(int, input().split()))
a = [0] * t
if w1 > w2:
    w1, w2 = w2, w1
a[t - 1] = w2
a[0] = w1
r = w1 + w2
if t % 2 == 1:
    b = t // 2
else:
    b = t // 2
for i in range(t - 2, b - 1, -1):
    a[i] = a[i + 1] + d
for i in range(1, t - 1):
    if a[i] == 0:
        a[i] = a[i - 1] + d
        r += a[i]
    elif a[i] - a[i - 1] > d:
        a[i] = a[i - 1] + d
        r += a[i]
    else:
        r += a[i]
        
print(r)

