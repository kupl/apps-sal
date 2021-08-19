from collections import Counter
n = int(input())
a = list(map(int, input().split()))
c = 0
b = []
for i in range(n):
    k = 1
    t = 0
    while a[i] % k == 0:
        k = k * 2
        t += 1
    b.append(t)
count = Counter(b)
p = count.most_common()
x = p[0][0]
print(n - p[0][1])
for i in range(n):
    if b[i] != x:
        print(a[i], end=' ')
