(v1, v2) = map(int, input().split())
(t, d) = map(int, input().split())
a = [0] * t
a[0] = v1
a[t - 1] = v2
for i in range(1, t - 1):
    a[i] = a[i - 1] + d
k = t - 1
while abs(a[k] - a[k - 1]) > d:
    if a[k] - a[k - 1] > 0:
        a[k - 1] = a[k] - d
    else:
        a[k - 1] = a[k] + d
    k -= 1
print(sum(a))
