n, k = map(int, input().split())
a = sorted(map(int, input().split()))
t = 0
x = 0
while max(a) > 2 * k:
    while a[x] <= 2 * k:
        x += 1
    if x > 0:
        k = max(k, a[x - 1])
    while 2 * k < a[x]:
        k *= 2
        t += 1
print(t)
