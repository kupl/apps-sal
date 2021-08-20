n = int(input())
a = list(map(int, input().split()))
count = [0] * 100
b = [0] * 200005
for (i, v) in enumerate(a):
    tot = 0
    while v % 2 == 0:
        v //= 2
        tot += 1
    count[tot] += 1
    b[i] = tot
m = max(count)
idx = count.index(m)
print(n - m)
for i in range(n):
    if b[i] != idx:
        print(a[i], end=' ')
