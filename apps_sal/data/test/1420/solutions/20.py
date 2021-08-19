(n, l) = map(int, input().split())
a = [int(i) for i in input().split()]
a.sort()
a += [l]
d = a[0]
for i in range(1, n + 1):
    x = a[i] - a[i - 1]
    if i != n:
        x /= 2
    d = max(d, x)
print(d)
