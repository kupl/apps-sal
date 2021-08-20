(n, m) = [int(i) for i in input().split()]
a = [0] * 300
for i in range(m, 300, m):
    a[i + 1] = 1
k = 0
while k < 299 and n > 0:
    k += 1
    if a[k] == 1:
        continue
    a[k] = 1
    n -= 1
for i in range(1, 300):
    if a[i] == 0:
        k = i - 1
        break
print(k)
