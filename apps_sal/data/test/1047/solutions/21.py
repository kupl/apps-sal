n = int(input())
m = 0
c = 1
i = n
while i > 0:
    m = max(m, i % 10)
    i = i // 10
a = [0] * m
i = n
while i > 0:
    for j in range(i % 10):
        a[j] += c
    c = c * 10
    i = i // 10
print(m)
for i in range(m):
    print(a[i], end=' ')
